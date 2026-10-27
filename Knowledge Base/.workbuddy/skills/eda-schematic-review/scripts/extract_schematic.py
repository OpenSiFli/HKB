# -*- coding: utf-8 -*-
"""
EDA 原理图 PDF 识别 - 方案A：矢量文本精准解析
依据 EDA原理图PDF识别提示词.md §2.1 执行（方案A 优先，方案B OCR 仅作兜底）。

仅使用 pdfplumber 读取 page.chars（文本/坐标/字号/字体），按 EDA 正则规则
筛选「位号 / 元件参数 / 网络标号 / 电源地」，输出结构化 JSON 与按坐标排版的纯文本。

用法:
    python extract_schematic.py <input.pdf> [output_dir]

  - input.pdf  必填：待解析的原理图 PDF 路径（相对/绝对均可）。
  - output_dir 可选：输出目录，默认与 input.pdf 同目录。

输出:
    <output_dir>/extract_A.json            结构化记录（含 page_num/extract_scheme/type/content/x/y/confidence/status）
    <output_dir>/schematic_struct_text.txt 按页、按 (top,x) 排序的文本行，便于人工/全文检索定位

方案判定:
    任一页 chars 数 < 30 即标记该页需切换方案B OCR（轮廓化/位图 PDF）。

注意：本脚本**不硬编码任何机器专属路径**，PDF 路径必须由命令行显式传入，
因此知识库整体拷贝到其他机器后可直接复用。
"""
import json
import re
import os
import sys
import pdfplumber

RE_REFDES = re.compile(r'\b([RCUJLDQTPBHF][A-Z]?\d+)\b')
RE_PARAM = re.compile(r'\b\d+(\.\d+)?\s?(k|M|u|n|p|m|K|U|N|P|µ)?(Ω|Ohm|F|V|A|H|Hz|MHz|kHz|K|%)\b', re.I)
RE_NET = re.compile(r'([A-Za-z0-9_]+[_\-/][A-Za-z0-9_+\-/]+|[A-Za-z0-9]+[+\-][A-Za-z0-9_]*)')
RE_POWER = re.compile(r'\b(VCC|VDD|VSS|GND|VBAT|VBUS|VSYS|AVDD|DVDD|VBATS|VDDIO|VCC\d|VDD\d|3V3|5V|1V8|1V2|V\d+_\w+)\b', re.I)


def cluster_lines(chars, tol_ratio=1.1):
    if not chars:
        return []
    chars = sorted(chars, key=lambda c: (round(c['top']), c['x0']))
    lines = []
    cur = [chars[0]]
    cur_top = chars[0]['top']
    cur_size = chars[0]['size']
    for c in chars[1:]:
        if abs(c['top'] - cur_top) <= max(cur_size, c['size']) * 0.6:
            cur.append(c)
        else:
            lines.append(cur)
            cur = [c]
            cur_top = c['top']
            cur_size = c['size']
    lines.append(cur)
    return lines


def main():
    if len(sys.argv) < 2:
        print("用法: python extract_schematic.py <input.pdf> [output_dir]")
        sys.exit(1)
    src = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(src))
    if not os.path.exists(src):
        print(f"[错误] 找不到输入 PDF: {src}")
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    out_json = os.path.join(out_dir, "extract_A.json")
    out_text = os.path.join(out_dir, "schematic_struct_text.txt")
    if os.path.exists(out_text):
        os.remove(out_text)

    records = []
    page_summaries = []
    with pdfplumber.open(src) as pdf:
        npages = len(pdf.pages)
        for pidx, page in enumerate(pdf.pages):
            chars = page.chars
            if len(chars) < 30:
                page_summaries.append({
                    "page_num": pidx + 1, "scheme": "B(待切换)",
                    "char_count": len(chars),
                    "note": "矢量文本极少，疑似轮廓化/位图，需切换方案B OCR",
                })
                continue
            lines = cluster_lines(chars)
            page_text_lines = []
            for line in lines:
                line.sort(key=lambda c: c['x0'])
                s = "".join(c['text'] for c in line)
                if not s.strip():
                    continue
                x0 = min(c['x0'] for c in line)
                top = line[0]['top']
                size = max(c['size'] for c in line)
                page_text_lines.append((top, x0, s, round(size, 1)))
                for m in RE_REFDES.finditer(s):
                    records.append({"page_num": pidx + 1, "extract_scheme": "方案A", "type": "位号",
                                    "content": m.group(1), "x": round(x0, 1), "y": round(top, 1),
                                    "confidence": 1.0, "status": "正常"})
                for m in RE_PARAM.finditer(s):
                    records.append({"page_num": pidx + 1, "extract_scheme": "方案A", "type": "元件参数",
                                    "content": m.group(0).strip(), "x": round(x0, 1), "y": round(top, 1),
                                    "confidence": 1.0, "status": "正常"})
                for m in RE_NET.finditer(s):
                    tok = m.group(0)
                    if len(tok) >= 2 and not RE_REFDES.fullmatch(tok):
                        records.append({"page_num": pidx + 1, "extract_scheme": "方案A", "type": "网络标号",
                                        "content": tok, "x": round(x0, 1), "y": round(top, 1),
                                        "confidence": 1.0, "status": "正常"})
                for m in RE_POWER.finditer(s):
                    records.append({"page_num": pidx + 1, "extract_scheme": "方案A", "type": "电源地",
                                    "content": m.group(1), "x": round(x0, 1), "y": round(top, 1),
                                    "confidence": 1.0, "status": "正常"})
            page_summaries.append({
                "page_num": pidx + 1, "scheme": "方案A", "char_count": len(chars),
                "line_count": len(page_text_lines), "note": "矢量文本解析成功",
            })
            with open(out_text, 'a', encoding='utf-8') as ft:
                ft.write(f"\n=== PAGE {pidx + 1} ===\n")
                for top, x0, s, size in sorted(page_text_lines):
                    ft.write(f"[{top:7.1f},{x0:7.1f},sz{size}] {s}\n")

    result = {
        "source": src,
        "scheme": "方案A（pdfplumber 矢量文本）",
        "pages_total": npages,
        "page_summaries": page_summaries,
        "records": records,
    }
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("PAGES:", npages)
    print("TOTAL RECORDS:", len(records))
    type_count = {}
    for r in records:
        type_count[r['type']] = type_count.get(r['type'], 0) + 1
    print("BY TYPE:", type_count)
    for ps in page_summaries:
        print(ps)


if __name__ == "__main__":
    main()
