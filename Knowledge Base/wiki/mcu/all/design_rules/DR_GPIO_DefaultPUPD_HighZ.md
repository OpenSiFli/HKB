---
title: DR-GPIO默认上下拉与高阻处理规范
type: mcu_design_rule
aliases: ["DR_GPIO_DefaultPUPD_HighZ","GPIO上下拉高阻设计规范"]
tags: ["企业MCU","通用设计规范","GPIO/信号","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_GPIO]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X GPIO 上电默认上下拉（PE 默认=1）、高阻配置、开漏与中断的设计规范，防止默认态冲突、悬空漏电与误触发。

## 核心硬件内容
### 1. 规范主题与适用范围
- 主题：GPIO 默认态、上下拉电阻、高阻态、开漏输出、中断使能。
- 适用：3.3V 系列 SF32LB52X 全部 45 个 GPIO（PA00–PA44，含 PA21）与电池系列 SF32LB52x 共 44 个 GPIO（**无 PA21**，pin24 为电源引脚 VCC）原理图与固件设计。

### 2. 设计要求
- 上电后 IO 默认存在上拉或下拉（PE=1），软件须配置为所需状态。典型默认态：PA03/PA11/PA12=PU、PA18=PU(SWDIO)、PA19=No Pull(SWCLK)，其余多为 PD（以手册表 5-1 为准）。
- 高阻配置：PE=0 + IO 设为 GPIO 功能 + GPIO 输出使能关闭。
- 开漏输出：使能内部上拉(PE=1,PS=1) 或外部上拉；开漏0=OE=1,O=0；开漏1=OE=0。
- 中断：不用时须关闭中断使能，避免误触发；中断条件由 IPH/IPL/ITR 配置。

### 3. 约束禁忌
- 使能输入功能的数字 IO 若悬空，低功耗电流升高 → 必须配置确定电平（接确定输出或上下拉）。
- 多个外设接口信号指定到同一 IO 会引起功能错误（PINMUX 配置须唯一）。
- 低功耗不用的输入脚须配置确定电平或上下拉，避免悬空。

### 4. 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §5（P64–P68，表 5-1、HPSYS_GPIO 寄存器）；原厂 Datasheet Table 5-1/5-2。

## 关联页面
- GPIO 外设：[[SF32LB52_Peripheral_GPIO]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_GPIO_Default_PUPD]]、[[CR_FloatingIO_LowPower]]、[[CR_Reset_Levels]]
- 低功耗：[[DR_LowPower_IO_Retention]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§5（P64–P68）
2. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，Table 5-1/5-2

## 待核实问题
- 完整 45 脚默认态以手册表 5-1 为准，审图/固件须逐脚核对。
