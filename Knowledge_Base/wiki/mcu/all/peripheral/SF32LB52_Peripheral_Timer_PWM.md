---
title: SF32LB52 外设-定时器与PWM
type: mcu_periph
aliases: ["SF32LB52X TIM","SF32LB52X PWM","SF32LB52X Timer"]
tags: ["企业MCU","外设模块-TIM/PWM","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
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
SF32LB52X 定时器资源：GPTIM1/2（16-bit 通用）、BTIM1/2（32-bit 基本）、ATIM1（32-bit 高级，6 路互补 PWM + 死区 + 刹车）、LPTIM1/2（24-bit 低功耗）、RTC、WDT1 + IWDT。本页整理 PWM 输出能力与电机/功率驱动相关电路约束。

## 核心硬件内容
### 1. 定时器特性（§3.6，P21–P24）
- **GPTIM（16-bit）**：4 通道，输入捕获/输出比较/PWM，预分频 1~65536，主从级联。
- **ATIM（32-bit 高级）**：6 通道；CH1~3 可输出 2 路带死区互补 PWM；CH4 单 PWM；CH5/6 输出比较；2 路刹车输入（快速进入安全态）；支持霍尔接口。
- **BTIM（32-bit 基本）**：定时，主从级联。
- **LPTIM（24-bit 低功耗）**：可在低功耗下计数/唤醒，预分频最高 128，支持 IO 边沿触发计数（可关内部时钟）。
- **WDT**：Mode0（到时直接复位，24-bit）、Mode1（先中断后复位，双周期 24-bit），写保护防误触。

### 2. 电路要求（PWM/功率相关）
- ATIM 互补 PWM + 死区 + 刹车适用于电机/半桥驱动；刹车信号源含 CPU lockup、外部输入、软件触发。
- PWM 输出引脚来自 GPIO PA（PA_TIM 复用组 Sel#=5），须正确配置 PINMUX 与驱动能力。
- 驱动功率负载须外加栅极驱动/桥电路，MCU 引脚仅作逻辑控制（驱动电流见 GPIO 页）。

### 3. 约束禁忌
- 互补 PWM 死区时间须按桥臂开关特性设置，避免直通。
- 刹车回路必须可靠，确保故障时快速关断输出到安全态。
- 低功耗场景由 LPTIM 唤醒时，IO 计数源须满足边沿/抗抖配置。

### 4. 规范依据
- Datasheet §3.6 Timers（P21–P24）、§1.3.3 地址映射（ATIM1 0x5000_4000、GPTIM1/2、BTIM1/2、LPTIM1/2、RTC、WDT1、IWDT，P4–P7）

## 用户手册 V0.8.8 补充（ATIM 紧急断路 / 6 步 PWM）
来源：[[SF32LB52X_UserManual_V0.8.8]] §9.1.3.14–15（P192）。

- **紧急断路（Break）**：用于保护 ATIM 驱动的功率开关。两路断路输入 **BKIN / BKIN2** 通常接功率级/三相逆变器故障输出；激活时关闭 PWM 输出并强制预定义安全态。BDTR_BKE/BKE2 置1 使能；BDTR_BKP/BKP2 选极性；BKIN 可在死区后强制输出为有效/无效电平，BKIN 可强制无效态。ATIM 复位后断路默认禁止、BDTR_MOE 低。
- **写保护**：断路电路含写保护（AF1_LOCK，3 级），可冻结死区、输出极性、禁止态、PWM 模式、断路使能/极性等参数。
- **6 步 PWM**：换向事件(COM) 预装载各通道配置，死区+互补输出机制保留；单脉冲模式(CR1_OPM) 可用于单次触发延时脉冲。
- 刹车回路必须可靠以确保故障快速关断（审图要点，见 [[CR_ATIM_Break_BKIN]]）。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设定时器/PWM（GPTIM/ATIM/BTIM/LPTIM/WDT、互补 PWM、刹车）硬件约束在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜电源：[[SF32LB52_Peripheral_Power]]
- 校验规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.6（P21–P24）、地址映射 Table 1-1（P4–P7）

## 待核实问题
- ATIM 各 PWM 通道与具体 GPIO 的引脚映射（Sel#=5 下）待补 PINMUX 表。
