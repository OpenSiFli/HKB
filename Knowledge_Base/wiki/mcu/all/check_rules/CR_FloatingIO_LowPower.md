---
title: CR-低功耗数字IO浮空
type: mcu_check_rule
aliases: ["CR_FloatingIO_LowPower","浮空输入审图规则"]
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
校验 SF32LB52X 中「使能了输入功能」的数字 IO 在低功耗场景下是否被配置为确定电平（接他芯确定输出或上/下拉电阻），避免悬空导致漏电/功耗升高。

## 核心硬件内容（背景）
Datasheet Table 5-1 注释明确：低功耗场景下，使能输入功能的数字 IO 若悬空，功耗会上升；须配置确定电压——接其他芯片的确定输出，或连接相应上拉/下拉电阻。详见 [[SF32LB52_Peripheral_GPIO]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X GPIO（PA00–PA44）被配置为输入功能（含 UART/I2C/SPI/定时器输入等复用）且引脚在原理图上悬空或仅靠内部上下拉时，结合功耗设计要求判定。
2. **违规现象描述**：输入功能引脚悬空无外部确定电平；或内部上下拉（7~20kΩ@3.3V）不足以在噪声环境下维持确定电平。
3. **风险影响说明**：浮空输入在低功耗模式漏电/功耗上升，电池供电产品续航劣化（一般/优化建议级）。
4. **标准化整改方案**：为悬空输入引脚加外部上拉/下拉电阻（阻值按总线要求，如 I2C 开漏必备上拉）；或连接至确定电平源；确认内部 PU/PD 使能是否合理。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_GPIO]]；Datasheet Table 5-1 注释（P39）、Table 4-3/4-4 内部上下拉电阻（P29–P30）。

## 关联页面
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 同类规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 5-1（P39）、Table 4-3/4-4（P29–P30）

## 待核实问题
- 各 GPIO 复位后默认状态（是否默认输入）待核实，以判定上电瞬时是否浮空。
