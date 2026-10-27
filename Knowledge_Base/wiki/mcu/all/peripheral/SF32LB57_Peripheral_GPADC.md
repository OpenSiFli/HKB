---
title: SF32LB57 GPADC（12-bit SAR ADC）
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_GPADC","SF32LB57 GPADC","SF32LB57 ADC"]
tags: ["企业MCU","外设-GPADC","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 集成 **1× 12-bit 通用 SAR ADC，共 12 通道，最高 4 Msps**，另有 **1× 片上温度传感器**。**两系列一致**；电池系列内部已分配一路 GPADC 通道检测 VBAT 电池电压。

## 1. 主要特性
- 类型：12-bit SAR ADC
- 通道数：**12 通道**
- 采样率：最高 **4 Msps**（Table 3-1）
- 片上温度传感器：1 个
- 参考电压：**GPADC_VREF(68)** 引脚，接电容到地，**不用外供电源**

## 2. 引脚（两系列一致）
| 引脚（QFN68） | 名称 | 类型 | 说明 |
|---|---|---|---|
| 68 | GPADC_VREF | A,I | GPADC 参考电压输入，接电容到地，**不用外供电源** |

**QFN80（3.3V 系列）**：GPADC_VREF = 63。

## 3. 硬件设计约束
- **GPADC_VREF(68) 必须接电容到地，禁止外部供电**。
- **外部信号源电阻须满足采样时间上限**：源电阻过大将导致采样电容充电不足、转换精度下降。⚠️ 本册（V0.2）**未给出具体 RAIN 限值**（SF32LB52 家族为 12-bit 最慢 5000kΩ / 最快 1kΩ@4 TPCLK），**不可直接套用**，待补。
- ADC 输入走线远离高频/射频（BRF_ANT、BUCK_LX 等）与数字开关信号，必要时加 RC 滤波。
- 未使用的 ADC 通道建议配置为确定电平或关闭，避免悬空引入漏电。
- 电池系列：**芯片内部已分配一路 GPADC 通道连接 VBAT(20)**，无需再从外部引到其它 GPADC 通道来检测电池电压。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 电源：[[SF32LB57_Peripheral_Power]]｜GPIO：[[SF32LB57_Peripheral_GPIO]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，产品特性「1×12-bit 通用 SAR ADC，共 12 通道」（P4）、Table 3-1（P38，GPADC 4Msps）、Table 4-22（P49，12-bit GPADC 电气特性）、Table 5-3（P61，GPADC_VREF=68）。
2. [DS5701-SF32LB57x V0.2]，同表（P4 / P38 / P50 / P62）。

## 待核实问题
1. **GPADC 源电阻（RAIN）上限**本册未给出，禁止套用 SF32LB52 数值，待补。
2. Table 4-22（12-bit GPADC 电气特性：INL/DNL/偏移/增益误差等）为表格渲染，本次未逐项转录，待 OCR/人工补录。
3. 12 个通道对应的具体 GPIO 引脚映射，待补 Pinmux / 用户手册。
