# -*- coding: utf-8 -*-
"""
Markdown → PDF 转换器（中文硬件评审报告专用，遵循《硬件评审报告排版与UI规范_V1.0》）。
用法:
    python md2pdf_report.py --md <input.md> --pdf <output.pdf> --title <标题> --date <YYYY-MM-DD>

v2 特性（2026-10-16 重设计）:
    - 思澈（SiFli）规格书风格封面：左上 logo、右侧黑主标题 + 红副题、版本/文档号、
      关键信息行（评审结论着色）、底部「重要说明」与公司落款。
      封面内容由 Markdown 中的 <!-- COVER ... --> 注释块驱动（不进入正文）。
    - 内容页页眉（左：报告标题；右：评审对象）与页脚（日期·版本 | Confidential | 页码），封面除外。
    - 正文可读性：H2 左侧色条 + 底部细线；「- **标签**：值」渲染为标签卡片行；
      「整体判定」渲染为判定横幅（通过=绿 / 有条件通过=琥珀 / 不通过=红）；
      PRJ 问题条目行左侧等级色条；表格按内容自动列宽、P0/P1/P2 等级词着色。
    - 中文字体自动探测（msyh.ttc → simsun.ttc → simhei.ttf），ttc 集合 index0/1 真粗体；
      可用 --font 指定。
    - 跳过 HTML 注释与 YAML frontmatter。
依赖: fpdf2, Pillow(仅 --trim-logo 时用到，运行时不强制)
"""
import re
import os
import sys
import argparse
from fpdf import FPDF

# ---------- 调色板 ----------
INK = (0, 0, 0)
GRAY = (110, 118, 126)
GRAY_LIGHT = (150, 156, 162)
PRIMARY = (44, 95, 138)          # #2C5F8A 主色（标签/标题条）
PRIMARY_BG = (238, 244, 249)     # #EEF4F9 标签底
BORDER = (214, 226, 238)         # #D6E2EE
RULE = (217, 217, 217)           # #D9D9D9
RED = (192, 0, 0)                # SiFli 副标题红 #C00000
AMBER = (176, 106, 0)            # P1 / 有条件通过
GREEN = (46, 139, 87)            # 通过
LEVEL_COLORS = {
    'P0': RED, '致命': RED,
    'P1': AMBER, '严重': AMBER,
    'P2': (31, 111, 178), '一般': (31, 111, 178),
    '优化': (0, 122, 102),
}
TABLE_HEADER_BG = (227, 237, 243)   # #E3EDF3
TABLE_ZEBRA = (246, 248, 250)       # #F6F8FA


def resolve_cjk_font(explicit=None):
    """返回 (字体路径, 是否ttc)。找不到则报错退出。"""
    if explicit:
        if not os.path.exists(explicit):
            sys.exit(f"[错误] 通过 --font 指定的字体文件不存在: {explicit}")
        return explicit, explicit.lower().endswith('.ttc')
    candidates = [
        r"C:/Windows/Fonts/msyh.ttc",
        r"C:/Windows/Fonts/simsun.ttc",
        r"C:/Windows/Fonts/simhei.ttf",
        r"C:/Windows/Fonts/msyh.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c, c.lower().endswith('.ttc')
    sys.exit(
        "[错误] 未找到可用的中文字体，无法生成中文 PDF。\n"
        "        请任选其一：\n"
        "        1) 在 Windows 上确保存在 msyh.ttc / simsun.ttc / simhei.ttf 之一；\n"
        "        2) 用 --font 指定一个支持中文的 TTF/TTC 绝对路径。\n"
        "        候选自动探测路径: " + ", ".join(candidates)
    )


def default_logo_path():
    here = os.path.dirname(os.path.abspath(__file__))
    cand = os.path.join(here, '..', 'assets', 'sifli_logo.png')
    return cand if os.path.exists(cand) else None


def clean_inline(text):
    """去掉行内代码反引号与 Obsidian 双链括号（** 加粗标记由 token 流单独处理）。"""
    return text.replace('`', '').replace('[[', '').replace(']]', '')


def parse_cover(md):
    """解析并移除 <!-- COVER ... --> 块，返回 (cover dict 或 None, 余下 md)。"""
    m = re.search(r'<!--\s*COVER\b(.*?)-->', md, flags=re.DOTALL)
    if not m:
        return None, md
    cover = {'rows': []}
    for ln in m.group(1).splitlines():
        ln = ln.strip()
        if not ln or ':' not in ln:
            continue
        k, v = ln.split(':', 1)
        k = k.strip().lower()
        v = v.strip()
        if k == 'row':
            parts = [p.strip() for p in v.split('|', 1)]
            if len(parts) == 2:
                cover['rows'].append(parts)
        else:
            cover[k] = v
    md = md[:m.start()] + md[m.end():]
    return cover, md


def cjk_len(s):
    return sum(2 if ord(ch) > 0x2E80 else 1 for ch in s)


def level_color(text):
    """仅当单元格是等级词本身或以 P0/P1/P2· 开头时着色，避免误染普通描述。"""
    t = text.strip()
    m = re.match(r'^(P[012])(?![A-Za-z0-9])', t)
    if m:
        return LEVEL_COLORS[m.group(1)]
    if t in ('致命', '严重', '一般', '优化'):
        return LEVEL_COLORS[t]
    return None


STATUS_COLORS = {
    '已闭环': GREEN, '通过': GREEN, 'PASS': GREEN,
    '待办': AMBER, '待验证': AMBER, '新建': AMBER,
    '不通过': RED,
    '建议': (31, 111, 178),
}


def status_color(text):
    """单元格为状态词本身时着色（待办=琥珀 / 已闭环=通过=绿 / 不通过=红）。"""
    return STATUS_COLORS.get(text.strip())


def verdict_color(text):
    t = text.strip()
    if '不通过' in t or '不建议' in t:
        return RED
    if '有条件' in t:
        return AMBER
    if '通过' in t or '关闭' in t:
        return GREEN
    return PRIMARY


class PDFReport(FPDF):
    def __init__(self, title, date, header_right='', footer_left=''):
        super().__init__(orientation='P', unit='mm', format='A4')
        self._title = title
        self._date = date
        self._header_right = header_right
        self._footer_left = footer_left
        self.set_margins(18, 20, 18)
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        if self.page_no() == 1:
            return
        # 页眉：左标题 / 右评审对象，下方细线
        self.set_y(9)
        self.set_font('CJK', '', 8)
        self.set_text_color(*GRAY)
        self.cell(0, 4.5, self._title, 0, 0, 'L')
        if self._header_right:
            self.set_xy(self.l_margin, 9)
            self.cell(0, 4.5, self._header_right, 0, 0, 'R')
        self.set_draw_color(*RULE)
        self.set_line_width(0.2)
        self.line(self.l_margin, 15, self.w - self.r_margin, 15)
        self.set_xy(self.l_margin, 20)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-14)
        self.set_draw_color(*RULE)
        self.set_line_width(0.2)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_y(-12.5)
        self.set_font('CJK', '', 8)
        self.set_text_color(*GRAY_LIGHT)
        if self._footer_left:
            self.cell((self.w - self.l_margin - self.r_margin) * 0.38, 5, self._footer_left, 0, 0, 'L')
        self.cell((self.w - self.l_margin - self.r_margin) * 0.34, 5, 'Confidential · 仅供内部评审使用', 0, 0, 'C')
        self.cell(0, 5, f'第 {self.page_no()} 页', 0, 0, 'R')


def _draw_checkbox(pdf, checked):
    x = pdf.get_x()
    y = pdf.get_y()
    s = 3.5
    pdf.set_draw_color(120, 120, 120)
    pdf.set_line_width(0.2)
    pdf.rect(x, y + 0.6, s, s)
    if checked:
        pdf.set_draw_color(46, 139, 87)
        pdf.set_line_width(0.45)
        pdf.line(x + 0.8, y + 0.6 + s / 2, x + 1.6, y + 0.6 + s - 0.7)
        pdf.line(x + 1.6, y + 0.6 + s - 0.7, x + s - 0.6, y + 0.6 + 0.9)
    pdf.set_xy(x + s + 1.2, y)


def tokenize(text):
    """把 **加粗** 文本拆成 (片段, style) 词元；拉丁串（含内部空格）成词、CJK 按字、单独空格保留。"""
    toks = []
    for part in re.split(r'(\*\*.*?\*\*)', text):
        if not part:
            continue
        style = 'B' if part.startswith('**') else ''
        body = part.strip('*')
        for m in re.finditer(r'[A-Za-z0-9_@./#&+µΩ±°%<>=\-–—:;()\[\]\'" ]+|\S', body):
            toks.append((m.group(0), style))
    return toks


def flow(pdf, text, width, line_h, size, color=INK, x=None, y=None, draw=True):
    """按宽度逐词元排版（支持加粗混排），返回结束 y。"""
    if x is None:
        x = pdf.get_x()
    if y is None:
        y = pdf.get_y()
    cx, cy = x, y
    for tok, style in tokenize(text):
        pdf.set_font('CJK', style, size)
        w = pdf.get_string_width(tok)
        if w <= 0:
            continue
        if cx + w > x + width + 0.1:
            if not tok.strip():  # 换行点上的纯空格直接吞掉
                cx = x
                cy += line_h
                continue
            cx = x
            cy += line_h
        if draw:
            pdf.set_text_color(*color)
            pdf.set_xy(cx, cy)
            pdf.cell(w, line_h, tok, ln=0)
        cx += w
    pdf.set_text_color(*INK)
    return cy + line_h


def build(md_path, pdf_path, title, date, font_path, is_ttc, logo_path=None):
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    cover, md = parse_cover(md)

    # 去掉其余 HTML 注释（含多行），不进入 PDF
    md = re.sub(r'<!--.*?-->', '', md, flags=re.DOTALL)

    header_right = (cover or {}).get('header', '')
    footer_left = f"评审日期：{date}" + (f" · {(cover or {}).get('version','')}" if (cover or {}).get('version') else '')

    pdf = PDFReport(title, date, header_right, footer_left)
    pdf.add_font('CJK', '', font_path, collection_font_number=0 if is_ttc else 0)
    pdf.add_font('CJK', 'B', font_path, collection_font_number=1 if is_ttc else 0)

    if cover:
        _render_cover(pdf, cover, logo_path)
        pdf.add_page()
    else:
        pdf.add_page()
        pdf.set_x(pdf.l_margin)
        pdf.set_font('CJK', 'B', 22)
        pdf.multi_cell(0, 10, title, align='C')
        pdf.set_x(pdf.l_margin)
        pdf.set_font('CJK', '', 10.5)
        pdf.set_text_color(*GRAY)
        pdf.multi_cell(0, 6, f'日期：{date}', align='C')
        pdf.set_text_color(*INK)
        pdf.ln(4)

    lines = md.splitlines()

    # 跳过 YAML frontmatter
    if lines and lines[0].strip() == '---':
        for _fm in range(1, len(lines)):
            if lines[_fm].strip() == '---':
                lines = lines[_fm + 1:]
                break

    avail = pdf.w - pdf.l_margin - pdf.r_margin
    h1_skipped = False

    # ---------- 各类块渲染 ----------

    def page_break_needed(h):
        return pdf.get_y() + h > pdf.h - pdf.b_margin - 6

    def render_h1(text):
        nonlocal h1_skipped
        if cover and not h1_skipped:
            h1_skipped = True  # 封面已承载文档标题，正文首个 H1 跳过
            return
        pdf.set_font('CJK', 'B', 16)
        pdf.ln(2)
        pdf.cell(0, 9, text, ln=True)
        pdf.ln(2)

    def render_h2(text):
        if page_break_needed(15):
            pdf.add_page()
        pdf.ln(2.0)
        y0 = pdf.get_y()
        # 左侧主色条
        pdf.set_fill_color(*PRIMARY)
        pdf.rect(pdf.l_margin, y0 + 0.5, 1.6, 7.5, 'F')
        pdf.set_font('CJK', 'B', 13)
        pdf.set_text_color(*PRIMARY)
        pdf.set_xy(pdf.l_margin + 4, y0)
        pdf.cell(0, 8.5, text, ln=True)
        pdf.set_text_color(*INK)
        pdf.set_draw_color(*RULE)
        pdf.set_line_width(0.2)
        pdf.line(pdf.l_margin, pdf.get_y() + 0.8, pdf.w - pdf.r_margin, pdf.get_y() + 0.8)
        pdf.ln(3.0)

    def render_h3(text):
        pdf.ln(1.2)
        if page_break_needed(10):
            pdf.add_page()
        pdf.set_font('CJK', 'B', 11.5)
        pdf.set_text_color(*PRIMARY)
        pdf.cell(0, 6.5, text, ln=True)
        pdf.set_text_color(*INK)
        pdf.ln(0.8)

    def render_paragraph(text):
        text = clean_inline(text)
        if not text.strip():
            return
        # PRJ 问题条目：左侧等级色条 + 缩进
        m = re.match(r'^\*\*(PRJ-\d+)\s*\[(P\d)', text)
        if m:
            c = LEVEL_COLORS.get(m.group(2), PRIMARY)
            if page_break_needed(14):
                pdf.add_page()
            y0 = pdf.get_y()
            end_y = flow(pdf, text, avail - 5, 5.2, 10.5, x=pdf.l_margin + 5)
            pdf.set_fill_color(*c)
            pdf.rect(pdf.l_margin, y0 + 0.4, 1.4, end_y - y0 - 1.6, 'F')
            pdf.set_xy(pdf.l_margin, end_y + 1.5)
            return
        end_y = flow(pdf, text, avail, 5.2, 10.5)
        pdf.set_xy(pdf.l_margin, end_y + 1.2)

    def render_label_rows(rows):
        """「- **标签**：值」→ 标签卡片行。整体判定 → 判定横幅。"""
        label_w = 26
        val_x = pdf.l_margin + label_w
        val_w = avail - label_w - 3
        for label, value in rows:
            value = clean_inline(value).strip()
            if label == '整体判定':
                _render_verdict_banner(value)
                continue
            pdf.set_font('CJK', 'B', 9.5)
            lab_lines = pdf.multi_cell(label_w - 3, 4.6, label, dry_run=True, output="LINES")
            end_y = flow(pdf, value, val_w, 4.8, 10, draw=False,
                         x=val_x + 1.5, y=pdf.get_y() + 1.5)
            h = max(len(lab_lines) * 4.6 + 3, end_y - pdf.get_y() + 1.5, 8)
            if page_break_needed(h + 2):
                pdf.add_page()
            y0 = pdf.get_y()
            # 标签格
            pdf.set_fill_color(*PRIMARY_BG)
            pdf.set_draw_color(*BORDER)
            pdf.set_line_width(0.2)
            pdf.rect(pdf.l_margin, y0, label_w, h, 'DF')
            pdf.set_xy(pdf.l_margin + 1.5, y0 + 1.5)
            pdf.set_font('CJK', 'B', 9.5)
            pdf.set_text_color(*PRIMARY)
            pdf.multi_cell(label_w - 3, 4.6, label, 0, 'L')
            # 值格
            pdf.set_fill_color(255, 255, 255)
            pdf.rect(val_x, y0, avail - label_w, h, 'DF')
            flow(pdf, value, val_w, 4.8, 10, x=val_x + 1.5, y=y0 + 1.5)
            pdf.set_xy(pdf.l_margin, y0 + h)
        pdf.ln(2.2)

    def _render_verdict_banner(value):
        c = verdict_color(value)
        h = 11
        if page_break_needed(h + 2):
            pdf.add_page()
        y0 = pdf.get_y()
        tint = (243, 249, 245) if c == GREEN else ((253, 247, 236) if c == AMBER else (251, 240, 240))
        pdf.set_fill_color(*tint)
        pdf.set_draw_color(*c)
        pdf.set_line_width(0.25)
        pdf.rect(pdf.l_margin, y0, avail, h, 'DF')
        pdf.set_fill_color(*c)
        pdf.rect(pdf.l_margin, y0, 2.2, h, 'F')
        pdf.set_font('CJK', 'B', 11.5)
        pdf.set_text_color(*c)
        pdf.set_xy(pdf.l_margin + 6, y0 + 2.8)
        pdf.cell(24, 6, '整体判定', 0, 0, 'L')
        pdf.cell(0, 6, value, 0, 0, 'L')
        pdf.set_text_color(*INK)
        pdf.set_xy(pdf.l_margin, y0 + h + 2.2)

    def render_table(table_lines):
        headers = [c.strip() for c in table_lines[0].split('|') if c.strip() != '']
        rows = []
        for line in table_lines[2:]:
            if '|' in line:
                rows.append([c.strip() for c in line.split('|') if c.strip() != ''])
        n = len(headers)
        # 按内容权重自动列宽 + 不可断词最小宽度（防止 PRJ-001 等被拆行）
        weights = []
        min_ws = []
        pdf.set_font('CJK', '', 9.2)
        for j in range(n):
            wmax = cjk_len(headers[j])
            tok_w = 0.0
            full_w = 0.0
            for r in [headers] + rows:
                cell = r[j] if j < len(r) else ''
                wmax = max(wmax, cjk_len(cell))
                full_w = max(full_w, pdf.get_string_width(cell))
                # 最长不可断词（按空格/·/、/；/｜切分）
                for tok in re.split(r'[\s·、；｜/]+', cell):
                    if tok:
                        tok_w = max(tok_w, pdf.get_string_width(tok))
            weights.append(max(wmax, 4))
            min_w = max(16.0, tok_w + 5.0)
            if full_w <= 30.0:  # 短整格（如 P1·待验证）不折行
                min_w = max(min_w, full_w + 5.0)
            min_ws.append(min_w)
        total = sum(weights)
        col_widths = []
        for j, wgt in enumerate(weights):
            wmm = avail * wgt / total
            col_widths.append(min(max(wmm, min_ws[j]), 78))
        if '等级' in ''.join(headers) and n >= 4:
            idx = next(k for k, h in enumerate(headers) if '等级' in h)
            col_widths[idx] = max(col_widths[idx], 24)
        # 归一化到 avail：只压缩/扩张高于各自最小宽度的列，不破坏最小宽度
        deficit = avail - sum(col_widths)
        if abs(deficit) > 0.3:
            flex = [max(col_widths[j] - min_ws[j], 0.0) for j in range(n)]
            pos = sum(flex)
            if pos > 0:
                for j in range(n):
                    if flex[j] > 0:
                        col_widths[j] += deficit * flex[j] / pos
            else:
                col_widths = [w * avail / sum(col_widths) for w in col_widths]

        font_size = 9.2
        line_h = font_size * 0.42

        def cell_height(text, width):
            pdf.set_font('CJK', '', font_size)
            lines_n = pdf.multi_cell(width - 3, line_h, clean_inline(text), dry_run=True, output="LINES")
            return max(line_h * 1.6, len(lines_n) * line_h + 2)

        trigger = pdf.h - pdf.b_margin - 12

        def draw_header(y0):
            pdf.set_font('CJK', 'B', font_size)
            pdf.set_fill_color(*TABLE_HEADER_BG)
            pdf.set_draw_color(*RULE)
            pdf.set_line_width(0.2)
            x0 = pdf.l_margin
            for j, h in enumerate(headers):
                cx = x0 + sum(col_widths[:j])
                pdf.rect(cx, y0, col_widths[j], h_header, style='DF')
                pdf.set_xy(cx + 1.5, y0 + 1.5)
                pdf.set_text_color(*INK)
                pdf.multi_cell(col_widths[j] - 3, line_h, h, 0, 'C')
            pdf.set_xy(pdf.l_margin, y0 + h_header)

        pdf.set_font('CJK', 'B', font_size)
        h_header = max(cell_height(h, col_widths[j]) for j, h in enumerate(headers))
        if pdf.get_y() + h_header > trigger:
            pdf.add_page()
        draw_header(pdf.get_y())

        pdf.set_font('CJK', '', font_size)
        for ri, row in enumerate(rows):
            cells = row[:n]
            h_row = max(cell_height(cells[j] if j < len(cells) else '', col_widths[j]) for j in range(n))
            if pdf.get_y() + h_row > trigger:
                pdf.add_page()
                draw_header(pdf.get_y())
                pdf.set_font('CJK', '', font_size)
            fill = TABLE_ZEBRA if ri % 2 == 1 else (255, 255, 255)
            pdf.set_fill_color(*fill)
            x0 = pdf.l_margin
            y0 = pdf.get_y()
            for j in range(n):
                cell = clean_inline(cells[j] if j < len(cells) else '')
                cx = x0 + sum(col_widths[:j])
                pdf.rect(cx, y0, col_widths[j], h_row, style='DF')
                pdf.set_xy(cx + 1.5, y0 + 1.5)
                c = level_color(cell) or status_color(cell)
                if c:
                    pdf.set_font('CJK', 'B', font_size)
                    pdf.set_text_color(*c)
                else:
                    pdf.set_font('CJK', '', font_size)
                    pdf.set_text_color(*INK)
                pdf.multi_cell(col_widths[j] - 3, line_h, cell, 0, 'L')
            pdf.set_xy(pdf.l_margin, y0 + h_row)
        pdf.set_text_color(*INK)
        pdf.ln(3)

    def render_bullet(text):
        text = clean_inline(text)
        if page_break_needed(10):
            pdf.add_page()
        y0 = pdf.get_y()
        pdf.set_font('CJK', '', 10.5)
        pdf.set_text_color(*PRIMARY)
        pdf.set_xy(pdf.l_margin, y0)
        pdf.cell(4, 5.2, '•', ln=0)
        pdf.set_text_color(*INK)
        end_y = flow(pdf, text, avail - 5.5, 5.2, 10.5, x=pdf.l_margin + 5.5)
        pdf.set_xy(pdf.l_margin, end_y + 0.8)

    def render_checkitem(text, checked):
        text = clean_inline(text)
        if page_break_needed(10):
            pdf.add_page()
        y0 = pdf.get_y()
        _draw_checkbox(pdf, checked)
        end_y = flow(pdf, text, avail - 5.5, 5.2, 10.5, x=pdf.l_margin + 5.5)
        pdf.set_xy(pdf.l_margin, end_y + 0.8)

    def render_blockquote(block_lines):
        text = ' '.join(l.strip().lstrip('>').strip() for l in block_lines if l.strip())
        text = clean_inline(text)
        if not text:
            return
        pdf.ln(1)
        start_y = pdf.get_y()
        end_y = flow(pdf, text, avail - 10, 5, 10, color=GRAY, x=pdf.l_margin + 7, draw=False)
        h = end_y - start_y + 3
        if page_break_needed(h + 2):
            pdf.add_page()
            start_y = pdf.get_y()
            end_y = start_y + h - 3
        pdf.set_fill_color(243, 248, 252)
        pdf.set_draw_color(*BORDER)
        pdf.set_line_width(0.2)
        pdf.rect(pdf.l_margin, start_y - 1, avail, h, 'DF')
        pdf.set_fill_color(*BORDER)
        pdf.rect(pdf.l_margin, start_y - 1, 1.2, h, 'F')
        flow(pdf, text, avail - 10, 5, 10, color=GRAY, x=pdf.l_margin + 7, y=start_y + 0.5)
        pdf.set_xy(pdf.l_margin, end_y + 2)

    # ---------- 主循环 ----------
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('---'):
            pdf.ln(1.5)
            pdf.set_draw_color(*RULE)
            pdf.set_line_width(0.2)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(3)
            i += 1
            continue
        if stripped.startswith('# ') and not stripped.startswith('## '):
            render_h1(stripped[2:])
            i += 1
            continue
        if stripped.startswith('## '):
            render_h2(stripped[3:])
            i += 1
            continue
        if stripped.startswith('### '):
            render_h3(stripped[4:])
            i += 1
            continue
        if stripped.startswith('>'):
            block = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                block.append(lines[i])
                i += 1
            render_blockquote(block)
            continue
        if stripped.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            render_table(table_lines)
            continue
        # 连续「- **标签**：值」合并为标签卡片组
        if stripped.startswith('- '):
            rows = []
            while i < len(lines):
                s2 = lines[i].strip()
                if not s2.startswith('- '):
                    break
                m = re.match(r'^- \*\*(.{1,14}?)\*\*[：:]\s*(.*)$', s2)
                if m:
                    rows.append((m.group(1), m.group(2)))
                    i += 1
                else:
                    break
            if rows:
                render_label_rows(rows)
                continue
            s2 = stripped
            if s2.startswith('- [ ]') or s2.startswith('- [x]') or s2.startswith('- [X]'):
                render_checkitem(s2[5:].strip(), s2[2] in ('x', 'X'))
                i += 1
                continue
            render_bullet(s2[2:])
            i += 1
            continue
        if stripped == '':
            pdf.ln(1.5)
            i += 1
            continue
        render_paragraph(stripped)
        i += 1

    pdf.output(pdf_path)
    print('PDF saved:', pdf_path)


def _render_cover(pdf, cover, logo_path):
    """思澈规格书风格封面。"""
    pdf.add_page()
    pdf.set_auto_page_break(False)  # 封面元素固定定位，禁止自动分页
    # 左上 logo
    if logo_path and os.path.exists(logo_path):
        pdf.image(logo_path, x=20, y=20, w=56)

    # 右侧标题区（黑主标题 + 红副题，镜像规格书封面）
    pdf.set_y(112)
    pdf.set_font('CJK', 'B', 26)
    pdf.set_text_color(*INK)
    pdf.cell(0, 13, cover.get('doc_title', ''), 0, 2, 'R')
    pdf.set_text_color(*RED)
    pdf.cell(0, 13, cover.get('doc_subtitle', ''), 0, 2, 'R')
    sub = '　'.join(x for x in [cover.get('version', ''), cover.get('doc_no', '')] if x)
    if sub:
        pdf.set_y(pdf.get_y() + 3)
        pdf.set_font('CJK', '', 11)
        pdf.set_text_color(*GRAY)
        pdf.cell(0, 7, sub, 0, 2, 'R')
    pdf.set_text_color(*INK)

    # 关键信息行
    pdf.set_y(168)
    label_w = 30
    for label, value in cover.get('rows', []):
        is_verdict = label in ('评审结论', '整体判定')
        pdf.set_font('CJK', '', 9.5)
        pdf.set_text_color(*GRAY)
        pdf.set_xy(pdf.l_margin, pdf.get_y())
        pdf.cell(label_w, 7.5, label, 0, 0, 'L')
        if is_verdict:
            c = verdict_color(value)
            pdf.set_font('CJK', 'B', 11)
            pdf.set_text_color(*c)
        else:
            pdf.set_font('CJK', 'B', 10.5)
            pdf.set_text_color(*INK)
        pdf.cell(0, 7.5, clean_inline(value), 0, 2, 'L')
        pdf.set_draw_color(*RULE)
        pdf.set_line_width(0.15)
        y = pdf.get_y()
        pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
        pdf.set_y(y + 2.2)
    pdf.set_text_color(*INK)

    # 重要说明（紧跟信息行之后，且不低于页面下部固定位置）
    disclaimer = cover.get('disclaimer', '')
    if disclaimer:
        pdf.set_y(max(pdf.get_y() + 12, pdf.h - 100))
        pdf.set_font('CJK', 'B', 10)
        pdf.set_text_color(*INK)
        pdf.cell(0, 6, '重要说明', ln=True)
        pdf.ln(1)
        y0 = pdf.get_y()
        end_y = flow(pdf, disclaimer, pdf.w - pdf.l_margin - pdf.r_margin - 8, 4.6, 8.5,
                     color=GRAY, x=pdf.l_margin + 4, draw=False)
        h = end_y - y0 + 4
        pdf.set_fill_color(246, 246, 246)
        pdf.set_draw_color(*RULE)
        pdf.set_line_width(0.15)
        pdf.rect(pdf.l_margin, y0, pdf.w - pdf.l_margin - pdf.r_margin, h, 'DF')
        flow(pdf, disclaimer, pdf.w - pdf.l_margin - pdf.r_margin - 8, 4.6, 8.5,
             color=GRAY, x=pdf.l_margin + 4, y=y0 + 2)
        pdf.set_text_color(*INK)

    # 底部落款
    pdf.set_y(-24)
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.2)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.set_y(-20)
    pdf.set_font('CJK', '', 8.5)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 4.5, 'SiFli Technologies (Nanjing) Co., Ltd.', 0, 2, 'C')
    pdf.set_text_color(*RED)
    pdf.cell(0, 4.5, 'http://www.sifli.com', 0, 2, 'C')
    pdf.set_text_color(*GRAY_LIGHT)
    pdf.cell(0, 4.5, 'Confidential · 仅供内部评审使用', 0, 2, 'C')
    pdf.set_auto_page_break(True, margin=18)  # 恢复正文自动分页


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md', required=True)
    ap.add_argument('--pdf', required=True)
    ap.add_argument('--title', default='原理图评审报告')
    ap.add_argument('--date', default='2026-01-01')
    ap.add_argument('--font', default=None,
                    help='中文字体 TTF/TTC 路径；默认自动探测 Windows 中文字体(msyh/simsun/simhei)')
    ap.add_argument('--logo', default=None,
                    help='封面 logo 图片路径；默认 <脚本目录>/../assets/sifli_logo.png')
    ap.add_argument('--no-cover', action='store_true', help='忽略 COVER 块，按旧版首页标题输出')
    args = ap.parse_args()
    font_path, is_ttc = resolve_cjk_font(args.font)
    logo = default_logo_path() if args.logo is None else (args.logo or None)
    if args.no_cover:
        logo = None
    build(args.md, args.pdf, args.title, args.date, font_path, is_ttc, logo_path=logo)


if __name__ == '__main__':
    main()
