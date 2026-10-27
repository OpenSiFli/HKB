---
title: CR-VBATS电池测量输入范围
type: mcu_check_rule
aliases: ["CR_VBATS_Range","VBATS审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_Datasheet_V0.2.6]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
校验 SF32LB52X 电池电压测量输入 VBATS（引脚 20，A,I）所接入电压不超过 0~4.7V 范围，避免过压损伤测量前端。

## 核心硬件内容（背景）
VBATS（引脚 20）为电池电压测量输入，额定范围 0~4.7V（特性见 §5 封装/电源，Table 5-3）。该引脚用于监测电池电压，不可当作主电源，且严禁输入超过 4.7V。详见 [[SF32LB52_Peripheral_Power]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X VBATS(20) 网络连接时，检查所接电池/分压网络最高电压是否 ≤4.7V，是否串接限流/分压保护。
2. **违规现象描述**：直接接入 >4.7V 电池（如 2 节锂电 7.4V 未分压）；或未做任何过压保护。
3. **风险影响说明**：过压 → 测量前端永久损伤，电池电量监测失效（严重）。
4. **标准化整改方案**：若电池电压 >4.7V，须经电阻分压后将送入 VBATS 的电压限制在 0~4.7V；加钳位保护；禁止将 VBATS 用作主电源输入。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_Power]]；Datasheet Table 5-3（VBATS 20，P47）、电源管理 §1.4（P8–P9）。

## 关联页面
- 电源：[[SF32LB52_Peripheral_Power]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 同类规则：[[CR_AbsMaxRatings]]、[[CR_PowerDomains]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 5-3（P47）、§1.4（P8–P9）

## 待核实问题
- VBATS 内部是否已带分压/钳位待核实；推荐外接分压比待补参考设计。
