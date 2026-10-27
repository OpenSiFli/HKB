---
title: CR-GPADC外部源电阻超限
type: mcu_check_rule
aliases: ["CR_GPADC_SourceResistance","GPADC源电阻审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-一般"]
sources: [[SF32LB52X_Datasheet_V0.2.6]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 一般
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
校验 SF32LB52X GPADC 输入通道（PA28~PA34 = CH0~CH6，及 VBATS）前端信号源等效电阻 RAIN 是否满足所选采样时间对应上限，否则转换精度下降。

## 核心硬件内容（背景）
12-bit GPADC 的采样电容要求外部源电阻 RAIN 与采样时间匹配（Table 4-19）：12-bit 下 TPCLK@24MHz 周期数 4→RAIN≤1kΩ、15→5kΩ、30→10kΩ、150→50kΩ、300→100kΩ、1500→500kΩ、15000→5000kΩ。详见 [[SF32LB52_Peripheral_GPADC]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 GPADC 输入引脚（PA28~PA34）前端的分压/滤波/传感器网络时，计算等效源电阻 RAIN，并与固件设定采样时间核对是否满足上表。
2. **违规现象描述**：前端电阻网络等效 RAIN 超过所选采样时间上限（如快速采样 4 TPCLK 却串入 >1kΩ）；或未考虑传感器输出阻抗。
3. **风险影响说明**：源电阻超限 → ENOB/SNDR 下降（单端 SNDR 约 61.96dB @无平均），采样值偏差（一般级精度风险）。
4. **标准化整改方案**：降低前端等效电阻（减小分压电阻/加缓冲运放），或延长采样时间（增加 TPCLK 周期数）使 RAIN 落在上限内；GPADC_VREF（68）稳定去耦。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_GPADC]]；Datasheet Table 4-19（P37）。

## 关联页面
- GPADC：[[SF32LB52_Peripheral_GPADC]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 同类规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 4-19（P37）

## 待核实问题
- GPADC_VREF 推荐电压与去耦值待核实。
