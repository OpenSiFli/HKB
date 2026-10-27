# -*- coding: utf-8 -*-
"""Generate CR_Checklist_* review-rule markdown files from the SF32LB52 official
hardware design Checklist. Each checklist item keeps its series applicability.
"""
import os, re

SRC = r"D:/.workbuddy/SF32LB52_Checklist.md"
OUT = r"D:/obsidian/硬件知识库/wiki/mcu/all/check_rules"
SRC_ALIAS = "SF32LB52_Checklist_V0.1_20241008"

# (output filename, label, risk_level, [related existing CR aliases])
SECTIONS = {
    ("封装", None):            ("CR_Checklist_Package", "封装", "一般", []),
    ("电源", "供电"):          ("CR_Checklist_Power", "电源-供电", "严重",
                                 ["CR_PowerDomains","CR_RefDesign_Batt_PowerTree","CR_RefDesign_Batt_OVP_Charger","CR_VBATS_Range","CR_AbsMaxRatings"]),
    ("电源", "功耗"):          ("CR_Checklist_PowerConsumption", "电源-功耗", "一般",
                                 ["CR_FloatingIO_LowPower","CR_Hibernate_SiP_Supply"]),
    ("时钟", None):            ("CR_Checklist_Clock", "时钟", "一般",
                                 ["CR_XTAL48M","CR_RefDesign_XTAL32K"]),
    ("存储", None):            ("CR_Checklist_Storage", "存储", "严重",
                                 ["CR_RefDesign_ExternalFlash_Power","CR_RefDesign_EMMC_SD_Pullup","CR_SDMMC_MPI2_Exclusive"]),
    ("射频", None):            ("CR_Checklist_RF", "射频", "一般",
                                 ["CR_BLE_RF_Antenna"]),
    ("多媒体", "显示"):        ("CR_Checklist_Display", "多媒体-显示", "一般",
                                 ["CR_RefDesign_LCD_FPC_EMI"]),
    ("多媒体", "音频"):        ("CR_Checklist_Audio", "多媒体-音频", "一般", []),
    ("通用接口", None):        ("CR_Checklist_Interface", "通用接口", "一般",
                                 ["CR_I2C_BusStuck","CR_USB_DPDM","CR_Reset_PWRKEY","CR_GPIO_Default_PUPD"]),
    ("硬件外部唤醒", None):    ("CR_Checklist_Wakeup", "硬件外部唤醒", "一般",
                                 ["CR_GPIO_Default_PUPD"]),
    ("调试和下载", None):      ("CR_Checklist_Debug", "调试和下载", "一般",
                                 ["CR_DebugInterface_PA18_PA19"]),
    ("EOS&ESD", None):        ("CR_Checklist_ESD", "EOS&ESD", "严重",
                                 ["CR_AbsMaxRatings"]),
    ("产线", None):            ("CR_Checklist_Production", "产线", "一般", []),
}

def norm_series(chip):
    if "电池" in chip:
        return "SF32LB52x(电池)"
    if "3.3V" in chip or "DUB6" in chip:
        return "SF32LB52X(3.3V)"
    if "所有" in chip:
        return "通用-两系列共用"
    return chip  # fallback, keep as-is

def clean(text):
    t = text.replace("<br>", "；").replace("\n", " ")
    t = re.sub(r"\s+", " ", t).strip()
    return t

lines = open(SRC, encoding="utf-8").read().splitlines()
cur_h2 = cur_h3 = None
header = None
# output: fname -> {"label","risk","related":[],"items":[(seq,item,chip_norm,chip_raw,point)], "subsections":[(h3,startidx)]}
data = {}

for ln in lines:
    s = ln.strip()
    if s.startswith("## "):
        cur_h2 = s[3:].strip(); cur_h3 = None; header = None; continue
    if s.startswith("### "):
        cur_h3 = s[4:].strip(); header = None; continue
    if not s.startswith("|"):
        continue
    cells = [c.strip() for c in s.strip("|").split("|")]
    # separator row (do NOT clear header: data rows follow it)
    if cells and set("".join(cells)) <= set("-: "):
        continue
    # header row detection
    if header is None and "序号" in cells and "适用芯片" in cells:
        header = cells; continue
    if header is None:
        continue
    # data row
    try:
        i_seq = header.index("序号")
        # item column: 核查事项 or 事项
        if "核查事项" in header:
            i_item = header.index("核查事项")
        else:
            i_item = header.index("事项")
        i_chip = header.index("适用芯片")
        i_point = len(cells) - 1  # last column = 核查要点 / 备注
    except ValueError:
        continue
    if len(cells) <= max(i_seq, i_item, i_chip, i_point):
        continue
    seq = clean(cells[i_seq]); item = clean(cells[i_item])
    chip_raw = clean(cells[i_chip]); chip_norm = norm_series(chip_raw)
    point = clean(cells[i_point])
    if not item:
        continue
    key = (cur_h2, cur_h3)
    if key not in SECTIONS:
        key = (cur_h2, None)  # fallback for combined sections (e.g. 通用接口)
        if key not in SECTIONS:
            continue
    fname, label, risk, related = SECTIONS[key]
    if fname not in data:
        data[fname] = {"label": label, "risk": risk, "related": related,
                       "items": [], "sub": cur_h3}
    data[fname]["items"].append((seq, item, chip_norm, chip_raw, point))
    # track current subsection for Interface combined file
    data[fname].setdefault("sub_h3", [])
    if data[fname]["sub_h3"] and data[fname]["sub_h3"][-1][0] == cur_h3:
        pass
    else:
        data[fname]["sub_h3"].append((cur_h3, len(data[fname]["items"]) - 1))

def series_set(items):
    s = set()
    for it in items:
        s.add(it[2])
    # order
    order = ["通用-两系列共用","SF32LB52X(3.3V)","SF32LB52x(电池)"]
    return [x for x in order if x in s] + [x for x in s if x not in order]

os.makedirs(OUT, exist_ok=True)
summary = []
for fname, info in data.items():
    items = info["items"]
    ss = series_set(items)
    rel = info["related"]
    rel_links = "\n".join(f"- [[{r}]]" for r in rel) if rel else "- （暂无既有 CR 直接对应，详见下方清单）"
    # build item tables; for combined Interface, split by subsection
    def table_block(sub_items):
        rows = []
        rows.append("| 序号 | 核查事项 | 适用芯片(系列) | 核查要点 |")
        rows.append("| -- |--|--|--|")
        for (seq, item, chip_norm, chip_raw, point) in sub_items:
            rows.append(f"| {seq} | {item} | {chip_norm} | {point} |")
        return "\n".join(rows)

    if fname == "CR_Checklist_Interface":
        # grouped by subsection
        body = ""
        # sub_h3 holds (h3, first_index)
        subs = info["sub_h3"]
        for si, (h3, start) in enumerate(subs):
            end = subs[si+1][1] if si+1 < len(subs) else len(items)
            grp = items[start:end]
            body += f"\n### {h3}\n\n" + table_block(grp) + "\n"
        item_section = body
    else:
        item_section = table_block(items)

    content = f"""---
title: CR-Checklist-{info['label']}
type: mcu_check_rule
aliases: ["{fname}","{info['label']}审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-{info['risk']}","来源-官方Checklist"]
sources: [[{SRC_ALIAS}]]
mcu_family: ["SF32LB52"]
series_applicability: {ss}
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: {info['risk']}
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SiFli 官方 **SF32LB52 硬件设计 Checklist（V0.1 20241008）**〈{info['label']}〉章节，提炼为原理图 AI 审图规则。共 {len(items)} 条核查事项，逐条保留官方「适用芯片」映射（已归一化为 { ' / '.join(ss) }），供设计评审与 PDF 原理图 AI 审图逐项核对。

## 核心硬件内容（背景）
本规则为官方黄金样板 Checklist 的同源转化，非本文独创。每条「核查要点」即官方对硬件设计的硬性/推荐要求；参数（电压范围、电容容值/耐压、线宽、上拉阻值、ESR/ppm、阻抗等）以官方 Checklist 原文为准。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析或设计评审时，逐项核对下方〈{info['label']}〉清单的每条「核查要点」。
2. **违规现象描述**：任一条「核查要点」未满足即视为违规（如电压越界、电容/线宽不达标、上拉缺失、IO 电平不匹配、布局/屏蔽违规、ESD 缺失等）。
3. **风险影响说明**：依条目性质而异——电源/存储/ESD 类违规可致器件永久损坏或功能失效（严重/致命）；时钟/射频/显示/音频类违规致性能劣化或 EMC 不通过（一般/优化）。
4. **标准化整改方案**：按各条目「核查要点」整改至满足官方参数（含选型、容值、线宽、布局、防护器件）。
5. **知识库溯源依据**：[[{SRC_ALIAS}]]（〈{info['label']}〉章节）。

{item_section}

## 关联页面
{rel_links}
- 来源摘要：[[{SRC_ALIAS}]]

## 原始来源完整引用
1. [SF32LB52 Checklist V0.1 20241008]，Raw：raw/mcu/all_chip/design_checklist/SF32LB52_Checklist_V0.1_20241008.md，章节：{info['label']}（共 {len(items)} 条）。

## 待核实问题
- 无（参数来自官方 Checklist 黄金样板）。
"""
    path = os.path.join(OUT, fname + ".md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    summary.append((fname, len(items), ss))

print("Generated %d CR files:" % len(summary))
for f, n, ss in summary:
    print(f"  {f}.md  items={n}  series={ss}")
