---
title: CR-参考设计-32.768kHz RTC晶振
type: mcu_check_rule
aliases: ["CR_RefDesign_XTAL32K","32K晶振审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-一般"]
sources: [[SF32LB52X_3V3_Reference_Schematic],[SF32LB52x_batt_Reference_Schematic],[SF32LB52_Peripheral_Clock]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 一般
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52 官方参考设计，校验 **32.768kHz RTC 晶振（XTAL32K_XI/XO，PA22/PA23）** 的负载电容、ESR 与频偏是否符合起振/计时精度要求。该晶振为可选（内部 RC 可作 RTC），但一旦使用须满足参数。

## 核心硬件内容（背景）
- 引脚：XTAL32K_XI = PA22，XTAL32K_XO = PA23。
- 参考设计实测取值：**负载电容 CL 7~12pF（推荐 8.8pF）**；**等效串联电阻 ESR ≤ 80KΩ（推荐 38KΩ）**；**频偏 ΔF/F0 ≤ ±10ppm**。
- 晶振须紧靠芯片、走线短且包地；与 48M 主晶振取值不同（48M 为 8.8pF / ±20ppm，见 [[CR_XTAL48M]]）。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到 XTAL32K_XI(PA22)/XTAL32K_XO(PA23) 网络连接 32.768k 晶振时触发。
2. **违规现象描述**：负载电容缺失/不匹配（不在 7~12pF）；ESR 过大（>80KΩ 起振困难）；频偏 >±10ppm（RTC 计时漂移）；晶振远离芯片、长走线未包地。
3. **风险影响说明**：不起振 → RTC 失效；频偏大 → 计时累积误差（一般）。
4. **标准化整改方案**：选 ESR ≤ 80KΩ 晶振；紧靠芯片、走线短且包地。**关于外部负载电容**：见下方「审图判读特别说明」——当 32K 晶体在推荐参数内或属 AVL 物料时，XI/XO 两端外部负载电容可不焊接；仅非推荐款才需外配（参考值 8.8pF）。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_Clock]]；[[CR_XTAL48M]]；参考设计两页（32K 晶振选型要求）。

## 审图判读特别说明 —— 外部负载电容并非必焊
**SiFli 全系 MCU 通用原则（与 48M 主晶振同）**：当 32.768k 晶体规格在芯片**推荐参数范围**内或属 SiFli **AVL** 物料时，`xtal_in` / `xtal_out`（即 XTAL32K_XI/XO）两端外部负载电容可不焊接，MCU 单独接晶体即可起振。

→ **AI 审图注意**：勿仅凭「XI/XO 未见对地负载电容」判违规。先确认晶体料号是否在推荐参数内 / AVL 内；在 → 判 PASS/N/A（片内匹配）；非推荐款才需按 CL 外配（参考官方 Checklist 第 4 条：CL 7pF 或 11.5pF、频偏 ≤±20ppm、ESR ≤80KΩ）。

## 关联页面
- 时钟：[[SF32LB52_Peripheral_Clock]]｜同类规则：[[CR_XTAL48M]]｜芯片实体：[[SF32LB52X]]、[[SF32LB52x_batt]]

## 原始来源完整引用
1. [SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf] / [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/，设计注释（32K 晶振 CL/ESR/ppm 取值）

## 待核实问题
- 无（参数来自参考设计黄金样板）。「外部负载电容非必焊」原则见 [[CR_XTAL48M]] 同名特别说明。
