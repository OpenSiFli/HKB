---
title: SF32LB52 外设-GPADC
type: mcu_periph
aliases: ["SF32LB52X ADC","SF32LB52X GPADC"]
tags: ["企业MCU","外设模块-ADC","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52x_Datasheet_V0.2.6],[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Datasheet_V2.5.5]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
series_applicability: ["通用-两系列共用"]
created: 2026-08-10
updated: 2026-08-11
---

## 摘要

> **适用系列**：本外设为 SF32LB52X（电池供电）与 SF32LB52x（3.3V 供电）两系列**共用**；两系列外设逻辑一致，差异仅在电源架构与电源专用引脚（见 [[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_GPIO]]）。
SF32LB52X 集成 1 路 12-bit SAR 型 GPADC，最高 4Msps，支持 7 路单端（PA28~PA34 = CH0~CH6）+ 1 路电池电压（VBATS）或 3 对差分输入。本页整理 GPADC 输入通道、参考电压与关键电路约束——尤其是外部信号源电阻与采样时间的硬性关系。

## 核心硬件内容
### 1. 工作机制
- 12-bit SAR ADC；单端输入 0~3.3V，差分 ‑2.1V~+2.1V。
- 支持单测/循环测，每帧 8 时隙可独立配置通道；支持软/硬件触发与 DMA。
- 通道映射：PA28=CH0、PA29=CH1、PA30=CH2、PA31=CH3、PA32=CH4、PA33=CH5、PA34=CH6；VBATS（引脚20）测电池电压。
- 参考电压：GPADC_VREF（引脚 68，A,I）。

### 2. 电路要求（关键约束）
**外部源电阻 RAIN 与采样时间关系（Table 4-19）** —— 必须满足，否则精度下降：

| 分辨率 | TPCLK@24MHz 周期数 | Tsample(ns) | 最大源电阻 RAIN(kΩ) |
|------|------|------|------|
| 12-bit | 4 | 166 | 1 |
| 12-bit | 15 | 625 | 5 |
| 12-bit | 30 | 1250 | 10 |
| 12-bit | 150 | 6250 | 50 |
| 12-bit | 300 | 12500 | 100 |
| 12-bit | 1500 | 62500 | 500 |
| 12-bit | 15000 | 625000 | 5000 |

- 采样率 fs = 1/(Tsample+Tconversion)；Tconversion≈125ns~10.67µs；最高 4Msps（差分 ENOB 10.6bit，单端 ENOB 10bit）。
- 前端RC滤波/分压网络的设计须使等效源电阻不超过上表对应采样时间上限。

### 3. 约束禁忌
- 输入电压严禁超过模拟输入范围（单端 0~3.3V），超限将损伤 ADC 或引入误差。
- 源电阻超限会降低 ENOB/SNDR（单端 SNDR 约 61.96dB @无平均）。
- GPADC_VREF（68）须提供稳定参考电压并去耦。

### 4. 规范依据
- Datasheet §3.2.1 12Bit ADC（P13）、Table 4-19 GPADC 电气特性（P37）、Table 5-2（PA28~PA34，P54–P55）、Table 5-3（GPADC_VREF 68，P47）

## 用户手册 V0.8.8 补充
来源：[[SF32LB52X_UserManual_V0.8.8]]（寄存器级，未新增电气参数）。

- 用户手册为寄存器/编程型，未对 GPADC 电气特性（源电阻表 Table 4-19、通道映射）做新增或修改，原 datasheet 约束全部有效。
- 补充提示：GPADC 输入通道 PA28~PA34（CH0~CH6）同时兼作部分唤醒源（WKUP_PIN0~6，见芯片实体页引脚表）；低功耗采样须注意通道与唤醒配置不冲突。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设 GPADC 电气特性（通道映射、源电阻表 Table 4-19、参考电压、采样率）在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜电源：[[SF32LB52_Peripheral_Power]]
- 校验规则：[[CR_GPADC_SourceResistance]]、[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.2.1（P13）、Table 4-19（P37）、Table 5-2（P54–P55）

## 待核实问题
- GPADC_VREF 推荐电压值与去耦方案，datasheet 文本未列，待核实。
