---
title: CR-散热裸焊盘EPAD未接地
type: mcu_check_rule
aliases: ["CR_EPAD_GND","EPAD接地审图规则"]
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
校验 SF32LB52X QFN68L 的散热裸焊盘 EPAD（引脚 69）是否在原理图与 PCB 上可靠连接至 GND。

## 核心硬件内容（背景）
QFN68L 封装底部中央为裸露散热焊盘 EPAD（引脚 69，Type=GND），须接 GND 以散热并保证焊接可靠性与电气参考。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X 封装 EPAD（引脚 69）符号时，检查其是否连接 GND 网络，并在 PCB 规则中检查是否开多过孔至内层地。
2. **违规现象描述**：EPAD 悬空、误接非 GND 网络、或仅单点连接未做热过孔阵列。
3. **风险影响说明**：散热不良 → 芯片过热降额/失效；焊接空洞 → 机械与电气不可靠（致命级可靠性风险）。
4. **标准化整改方案**：EPAD 接 GND，PCB 上布置足够数量的热过孔阵列连接至内层地平面；回流焊按 Table 5-4~5-6 曲线（峰值 240°C 无铅）。
5. **知识库溯源依据**：[[SF32LB52x_batt|SF32LB52x]] 专用引脚表；Datasheet Table 5-3（EPAD 69，P47）、Table 5-4~5-6 回流焊（P49–P50）。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜电源：[[SF32LB52_Peripheral_Power]]
- 同类规则：[[CR_PowerDomains]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 5-3（P47）、Table 5-4~5-6（P49–P50）

## 待核实问题
- EPAD 推荐过孔数量/直径待补封装 Layout 指南（Fig 5-2）。
