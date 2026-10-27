---
title: CR-多电源域供电缺失/超范围
type: mcu_check_rule
aliases: ["CR_PowerDomains","电源域审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-致命"]
sources: [[SF32LB52X_Datasheet_V0.2.6]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 致命
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
校验 SF32LB52X 多电源域（PVDD/VDDIOA/AVDD33/AVDD33_AUD/AVDD_BRF/VDD_SIP/VDD_RET/VDD_RTC）是否全部按型号正确供电且在额定范围内。

## 核心硬件内容（背景）
SF32LB52X 为多电源域 MCU，各电源引脚必须分别接入对应电压；PVDD 取值随型号（3.3V 或 1.8V）。任一电源缺失/短路/超范围将导致功能异常或永久损伤。详见 [[SF32LB52_Peripheral_Power]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 SF32LB52X 的电源引脚（19 PVDD、21 VDDIOA、14 AVDD33、38 AVDD33_AUD、52 AVDD_BRF、23 VDD_SIP、13 VDD_RET、12 VDD_RTC）时，核对每路是否连接、网络标号电压是否与型号匹配、是否有去耦电容。
2. **违规现象描述**：某电源引脚悬空/误接其他电压域/未加去耦；PVDD 电压与订购型号（3.3V 型如 BU36/BU56/EUB6/GUC6/JUD6，或 1.8V 型 DUB6）不一致；AVDD33/AVDD33_AUD/AVDD_BRF 不在 2.97~3.63V。
3. **风险影响说明**：电源缺失或错接 → 芯片不启动/部分子系统失效/闩锁或永久烧毁（致命）。
4. **标准化整改方案**：补全对应电源网络并按型号取电（3.3V 或 1.8V）；每路加推荐去耦电容；AVDD 类加低噪声滤波；核对 Table 5-7 型号电压。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_Power]]；Datasheet Table 4-1/4-2（P29）、Table 5-3（P47）、Table 5-7（P50）。

## 关联页面
- 电源：[[SF32LB52_Peripheral_Power]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜报告模板：[[index_MCU_ALL]]
- 同类规则：[[CR_AbsMaxRatings]]、[[CR_EPAD_GND]]、[[CR_VBATS_Range]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 4-1/4-2（P29）、Table 5-3（P47）、Table 5-7（P50）

## 待核实问题
- 各电源域推荐去耦电容容值待补参考设计。
