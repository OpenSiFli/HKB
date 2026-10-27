---
title: FC-Hibernate合封存储漏电
type: mcu_fault
aliases: ["FC_Hibernate_SiP_Leakage","Hibernate合封存储漏电故障"]
tags: ["企业MCU","故障案例","根因分析","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Power]]
mcu_family: ["SF32LB52"]
series_applicability: ["SF32LB52X(3.3V)"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 严重
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X（**3.3V 系列**，有 PA21）进入 hibernate 模式时，若合封存储外部供电（VDD_SIP）未被 PA21 控制关断，将持续漏电导致待机电流异常，本文给出根因与规避。**注意：电池系列 SF32LB52x 无 PA21，本故障案例不适用于该系列。**

## 核心硬件内容（背景）
- 故障所属电路模块：电源/低功耗（合封存储外部供电）。
- 相关芯片与硬件版本：SF32LB52X 采用外部供电合封存储的型号，用户手册 V0.8.8（§3.2）。

## 专项业务内容 —— 故障复盘（必填）
1. **失效现象、复现条件**：设备进入 hibernate 后待机电流远高于标称（2uA 级），电池快速耗尽；复现于"合封存储外部供电 + 使用 hibernate 模式"。
2. **涉及 MCU 型号、硬件版本**：SF32LB52X 家族（QFN68L），手册 V0.8.8。
3. **根因硬件分析**：hibernate 下芯片大部分供电关闭仅 PMUC/RTC/IWDT 工作；若 VDD_SIP 外部供电不能被关闭（如常开 LDO），合封存储持续耗电。正确做法：该供电在外部被 **PA21** 控制（hibernate 下 PA21 高阻，外部下拉关断开关；退出后 PA21 输出高开启供电）。
4. **短期整改方案、长期设计规避规则**：VDD_SIP 外部电源开关使能接 PA21 并加下拉确保 hibernate 关断；或在不用 hibernate 时改用 deepsleep/standby；软件保证退出 hibernate 后 PA21 输出高开启供电。
5. **同类图纸审图拦截规则**：对应 [[CR_Hibernate_SiP_Supply]]（Hibernate 合封供电控制）。

## 跨系列与存储介质说明（补充裁定）
- **存储介质类型决定是否需要断电**：PA21 主要给外挂 Flash 存储做电源控制。若外挂 **Nor Flash**，自身可进 **Deep Power Down（≈1µA）**，**可常供电**无需断电即低功耗，本漏电故障对 Nor 场景不必然发生；若外挂 **SPI Nand / SD Nand Flash**，自身无深度掉电机制，**必须控制供电**（PA21 或等效 GPIO 断电）才能避免持续漏电。
- **电池系列（SF32LB52x）替代方案**：无 PA21，外挂存储供电控制改选**默认 PU（上拉）的 GPIO** 驱动电源开关使能。详见 [[SF32LB52_Peripheral_Memory]] §4.1。

## 关联页面
- 电源外设：[[SF32LB52_Peripheral_Power]]｜设计规范：[[DR_LowPower_IO_Retention]]、[[DR_PowerArchitecture]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_Hibernate_SiP_Supply]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P42（§3.2，避免合封 IO 漏电）

## 待核实问题
- 无。
