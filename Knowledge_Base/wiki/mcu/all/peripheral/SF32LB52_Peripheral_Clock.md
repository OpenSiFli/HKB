---
title: SF32LB52 外设-时钟与晶振
type: mcu_periph
aliases: ["SF32LB52X Clock","SF32LB52X XTAL"]
tags: ["企业MCU","外设模块-时钟","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
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
SF32LB52X 主时钟由片内 48MHz 晶振（XTAL48M_XI/XO，引脚 55/54）提供，低速时钟可选 32.768kHz 晶振（PA22=XTAL32K_XI / PA23=XTAL32K_XO 或 XTAL32K_EXT）。本页整理晶振接口电路约束与选型要点。

## 核心硬件内容
### 1. 工作机制
- HCPU 最高 240MHz、LCPU 最高 24MHz，均由时钟架构（Fig 1-2）经 PLL/分频产生；主参考为 48MHz 晶振。
- 低速 32k 时钟可选：片外 32.768kHz 晶振接 PA22/PA23，或外部时钟 XTAL32K_EXT（PA25 复用）。

### 2. 标准电路要求
- **48MHz 晶振（引脚 55 XTAL48M_XI / 54 XTAL48M_XO）**：典型并接负载电容；具体晶振负载电容/匹配值见参考设计（datasheet 文本未列，待核实）。
- **32.768kHz 晶振（PA22/PA23）**：低速 RTC 时钟；或采用 XTAL32K_EXT 外部时钟源。
- 晶振走线应尽量短、远离数字/RF 噪声源，做好包地处理。

### 3. 约束禁忌
- XTAL48M 引脚（55/54）为敏感模拟节点，禁止直接驱动或并联不匹配电容导致起振失败/频偏。
- 旁路/负载电容选型须匹配晶振规格，否则影响起振与精度。
- 低速时钟若使用 GPIO 复用（PA22/PA23/PA25），复用配置优先级须正确设置（Sel#=8）。

### 4. 规范依据
- Datasheet §1.3.2 Clock Architecture（P3，Fig 1-2）、Table 5-2（PA22/PA23/PA25，P53）、Table 5-3（XTAL48M_XI/XO 引脚 55/54，P47）

## 用户手册 V0.8.8 补充（时钟细节）
来源：[[SF32LB52X_UserManual_V0.8.8]] §2、§3.4（P20–P46）。

- 低速时钟可由 **LRC10**（片内 10K RC）或 **LRC32**（32K RC）提供；XTAL32K 控制寄存器 LXT_CR 支持 EXT_EN（外部 32K 来自引脚）、CAP_SEL 等。
- 音频时钟可选 **XTAL48M** 或专用 **Audio PLL**（后者可微调频率，支持 48kHz 以下任意采样率；前者仅 48k 整数倍）。
- 主系统时钟 clk_hrc48 = 48MHz 片内 RC；高速时钟由 DLL1/2/3 产生（最高供 HCPU 240MHz）。

> 48M/32k 晶振负载电容、匹配电阻具体值手册仍未给出，仍为待核实（需补参考设计）。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设相关硬件参数（时钟架构、48M/32k 晶振接口、PLL/分频、音频时钟可选源）在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异（订购码 520/523/525/527 vs 52B/D/E/G/J）、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 电源：[[SF32LB52_Peripheral_Power]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]
- 校验规则：[[CR_XTAL48M]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§1.3.2（P3）、Table 5-2（P53）、Table 5-3（P47）

## 待核实问题
- 48MHz / 32.768kHz 晶振负载电容、驱动电平、起振电路具体参考值，待补 SiFli 参考设计。
