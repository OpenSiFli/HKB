# -*- coding: utf-8 -*-
"""
方案A 歧义消歧工具：给定目标位号/子串，提取其在 PDF 中的精确坐标，
并输出其周边包围盒内的所有单词（含坐标），用于消解方案A 合并文本造成的
"同名/相邻元件误并为一行"误读。

典型误读案例：WS501 原理图中，方案A 合并文本把晶体侧的 `C324` 与同行
`LP5308QVF` 充电器合并为一行、并记录充电器侧坐标，导致 v3 误判
"C324 属 LP5308 充电器、非晶体负载电容"。用本工具按坐标精确定位后确认
C323/C324 即 Y300 两端负载电容且双双 DNP。

用法:
    python probe_component.py --pdf <input.pdf> --target <Y300|C324|AW3512> [--padx 200] [--pady 170] [--page 3]

依赖: pdfplumber
"""
import argparse
import pdfplumber


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--target', required=True, help='要定位的位号或子串')
    ap.add_argument('--padx', type=float, default=200.0, help='包围盒水平半宽(pt)')
    ap.add_argument('--pady', type=float, default=170.0, help='包围盒竖直半宽(pt)')
    ap.add_argument('--page', type=int, default=None,
                    help='限定页码(1-based)；默认搜索全部页')
    args = ap.parse_args()

    with pdfplumber.open(args.pdf) as pdf:
        pages = pdf.pages
        if args.page:
            pages = [p for p in pages if p.page_number == args.page]
        for page in pages:
            words = page.extract_words(use_text_flow=False,
                                       keep_blank_chars=False)
            hit = next((w for w in words if args.target in w['text']), None)
            if not hit:
                continue
            print(f"=== Page {page.page_number}: found '{hit['text']}' "
                  f"bbox=({hit['x0']:.1f},{hit['top']:.1f})-"
                  f"({hit['x1']:.1f},{hit['bottom']:.1f}) ===")
            cx = (hit['x0'] + hit['x1']) / 2
            cy = (hit['top'] + hit['bottom']) / 2
            x0, x1 = cx - args.padx, cx + args.padx
            y0, y1 = cy - args.pady, cy + args.pady
            box = [w for w in words
                   if x0 <= w['x0'] <= x1 and y0 <= w['top'] <= y1]
            box.sort(key=lambda w: (round(w['top']), w['x0']))
            print(f"-- words in box x[{x0:.0f},{x1:.0f}] "
                  f"y[{y0:.0f},{y1:.0f}] --")
            for w in box:
                print(f"  ({w['x0']:7.1f},{w['top']:7.1f}) {w['text']!r}")
            return
    print(f"target '{args.target}' not found in {args.pdf}")


if __name__ == '__main__':
    main()
