---
title: CR-48MHz主晶振电路
type: mcu_check_rule
aliases: ["CR_XTAL48M","48M晶振审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_Datasheet_V0.2.6],[SF32LB52X_3V3_Reference_Schematic],[SF32LB52x_batt_Reference_Schematic]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-10
updated: 2026-08-13
---

## 摘要
校验 SF32LB52X 主时钟 48MHz 晶振接口（XTAL48M_XI 引脚55 / XTAL48M_XO 引脚54）的晶振、负载电容与走线是否符合起振要求。

## 核心硬件内容（背景）
主参考时钟由片内 48MHz 晶振（引脚 55 XI / 54 XO）提供，HCPU/LCPU 与各外设时钟均由其派生。晶振不起振或频偏将导致系统无法运行或通信异常。详见 [[SF32LB52_Peripheral_Clock]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X 的 XTAL48M_XI(55)/XTAL48M_XO(54) 网络连接时，检查是否连接 48MHz 晶振及两端负载电容、是否直连其他驱动源。
2. **违规现象描述**：未接晶振或负载电容缺失/不匹配；XI/XO 被误用作普通 GPIO 或并接不匹配电容；晶振远离芯片、长走线未包地。
3. **风险影响说明**：不起振 → 系统完全无法启动；频偏 → 通信误码/蓝牙性能劣化（严重）。
4. **标准化整改方案**：晶振紧靠芯片、走线短且包地；严禁在 XI/XO 施加外部驱动。**关于外部负载电容**：见下方「审图判读特别说明」——当晶体在推荐参数内或属 AVL 物料时，XI/XO 两端外部负载电容可不焊接；仅非推荐款晶体才需按 CL 外配（参考值：负载电容 8.8pF，频偏 ΔF/F0 ≤ ±20ppm）。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_Clock]]；Datasheet §1.3.2（P3）、Table 5-3（P47）；官方 Checklist（时钟章 第 1/2 条）。

## 审图判读特别说明 —— 外部负载电容并非必焊
**SiFli 全系 MCU 通用原则**：当所采用晶体的规格落在芯片**推荐参数范围**内，或选用 SiFli **AVL（认可物料清单）** 内的晶体料号时，`xtal_in` / `xtal_out`（即 XTAL48M_XI/XO）两端的**外部负载电容可以不焊接**——片内已集成匹配/负载电容或所选晶体为匹配型，MCU 单独接晶体即可正常起振。

→ **AI 审图注意**：**严禁**仅凭「XI/XO 两端未见对地负载电容」直接判违规。正确流程：
1. 先确认原理图所选晶体料号：是否在推荐参数内 / 是否在 AVL 内；
2. 若在 → 无外配负载电容属正常设计，判 **PASS / N/A（片内匹配）**；
3. 若为非推荐款（规格超出推荐范围）→ 才需按晶体 CL 外配负载电容（参考官方 Checklist 第 2 条：CL 7~12pF、频偏 ≤±10ppm、ESR ≤30Ω），否则判缺失/不匹配。

## 关联页面
- 时钟：[[SF32LB52_Peripheral_Clock]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜电源：[[SF32LB52_Peripheral_Power]]
- 同类规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§1.3.2（P3）、Table 5-3（P47）

## 待核实问题
- 48MHz 晶振「需外配负载电容」时的参考值：负载电容 **8.8pF**，频偏 ΔF/F0 ≤ **±20ppm**（来源：[[SF32LB52X_3V3_Reference_Schematic]]、[[SF32LB52x_batt_Reference_Schematic]]）。**但**：若晶体在推荐参数内或属 AVL 物料，外部负载电容可不焊接（见上方「审图判读特别说明」），此时「无外配电容」属正常设计而非缺陷。
