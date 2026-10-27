---
title: CR-绝对最大额定值超限
type: mcu_check_rule
aliases: ["CR_AbsMaxRatings","绝对最大额定值审图规则"]
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
校验 SF32LB52X 所有电源与 IO 网络电压不得超过绝对最大额定值（+3.63V / ‑0.3V，RF 输入 0dBm），防止永久损伤。

## 核心硬件内容（背景）
Absolute Maximum Ratings（Table 4-2）：PVDD/AVDD33/AVDD33_AUD/AVDD_BRF/VDDIOA 均为 ‑0.3V ~ +3.63V；VSS=0V；RF 输入 0dBm max；存储温度 ‑40~+125°C。任何瞬时过压都将造成不可逆损伤。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X 任意电源/IO 引脚网络连接时，检查是否有高于 +3.63V 的电源直接接入、是否存在负压风险（如感性负载反电动势未钳位）、RF 引脚是否可能注入 >0dBm。
2. **违规现象描述**：电源网络标称 >3.63V 直连芯片引脚；IO 引脚未做负压/过压保护；RF 天线端未限幅。
3. **风险影响说明**：超出绝对最大值 → 栅氧化层击穿/永久损坏（致命），且不可靠复现。
4. **标准化整改方案**：串接 LDO/电平转换器将电压限制在 3.63V 内；IO 侧加钳位二极管/TVS；RF 端加限幅与 ESD 保护；确保上电时序避免负压瞬态。
5. **知识库溯源依据**：[[SF32LB52x_batt|SF32LB52x]] 极限电气参数；Datasheet Table 4-2（P29）。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜电源：[[SF32LB52_Peripheral_Power]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]
- 同类规则：[[CR_PowerDomains]]、[[CR_VBATS_Range]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 4-2（P29）

## 待核实问题
- 各 IO 具体耐受瞬态能量待补 HBM/CDM 等级应用指南（Table 4-5：HBM ±4kV / CDM ±1kV）。
