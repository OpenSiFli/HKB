---
title: SF32LB57 定时器与 PWM
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Timer_PWM","SF32LB57定时器","SF32LB57 PWM"]
tags: ["企业MCU","外设-定时器/PWM","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 定时器资源（§3.6）：**2×16b GPTIM、4×32b BTIM、2×32b ATIM、2×24b LPTIM、1×PWM、1×RTC、2×24b WDT、1×IWDT**。**两系列一致**。

## 1. 定时器清单
| 类型 | 数量 | 位宽 | 说明 |
|---|---|---|---|
| GPTIM（通用定时器） | 2 | 16 bit | 通用定时/计数 |
| BTIM（基本定时器） | 4 | 32 bit | |
| ATIM（高级定时器） | 2 | 32 bit | 支持互补输出/刹车等高级功能（详见用户手册） |
| LPTIM（低功耗定时器） | 2 | 24 bit | 低功耗域可运行 |
| PWM | 1 | — | |
| RTC | 1 | — | 实时时钟 |
| WDT（看门狗） | 2 | 24 bit | |
| IWDT（独立看门狗） | 1 | — | |

## 2. 硬件设计约束
- PWM/定时器输出引脚由 GPIO 复用决定，须与 [[SF32LB57_Pinmux]] 核对。
- 高级定时器（ATIM）若用于电机/电源控制，注意互补输出死区与刹车（BKIN）输入的硬件连接（SF32LB52 家族有 ATIM 断路 BKIN 相关规则，57 家族待补）。
- 低功耗场景下 LPTIM 与 RTC 可在低功耗域保持运行，用于唤醒。
- 看门狗溢出复位须在硬件上保证可恢复（复位电路、喂狗策略）。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- GPIO/复用：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Pinmux]]
- 时钟：[[SF32LB57_Peripheral_Clock]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，§3.6 定时器（P21–24，含 3.6.1 通用 / 3.6.2 高级 / 3.6.3 基本 / 3.6.4 低功耗 / 3.6.5 看门狗）；产品特性定时器段（P4–5）。
2. [DS5701-SF32LB57x V0.2]，同上（P21–24 / P4–5）。

## 待核实问题
1. 各定时器实例的通道数、引脚映射与 ATIM 刹车（BKIN）硬件要求，待补用户手册与 Pinmux。
2. 复位与低功耗唤醒时序相关说明缺失。
