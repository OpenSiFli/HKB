---
title: CR-Hibernate合封存储供电控制(PA21)
type: mcu_check_rule
aliases: ["CR_Hibernate_SiP_Supply","合封存储Hibernate供电审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
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
校验 SF32LB52X（**3.3V 系列**，有 PA21）合封存储外部供电（VDD_SIP）由 PA21 控制，避免进入 hibernate 模式时外部电源无法关断导致漏电。**注意：电池系列 SF32LB52x 无 PA21，本规则不适用于该系列**（其 SiP 供电须以其他可控方式关断）。

## 核心硬件内容（背景）
若合封存储器采用外部供电，为保证芯片进入 hibernate 模式时不漏电，该供电应在外部被 **PA21** 控制（如 PA21 作外部电源开关使能）。进入 hibernate 后 PA21 表现为高阻，外部下拉电阻使电源开关关闭；退出后 PA21 自动输出高电平开启供电。若外部供电不能被关闭，应避免使用 hibernate 模式。详见 [[DR_LowPower_IO_Retention]]、[[SF32LB52_Peripheral_Power]] §硬性约束。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 VDD_SIP（引脚23）由外部电源经开关/LDO 供电，且设计使用 hibernate 模式时，核对使能控制是否接 PA21 并有确定下拉。
2. **违规现象描述**：① VDD_SIP 外部电源使能未接 PA21（如常开），hibernate 下持续漏电；② PA21 在 hibernate 下高阻但外部无下拉，开关态不确定；③ 既用 hibernate 又用不可关断的外部 VDD_SIP 供电。
3. **风险影响说明**：hibernate 漏电 → 待机电流异常升高、电池快速耗尽（严重）。
4. **标准化整改方案**：VDD_SIP 外部电源开关使能接 PA21，外部加下拉确保 hibernate 关断；或在不用 hibernate 时改用 deepsleep/standby；软件保证退出 hibernate 后 PA21 输出高开启供电。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P42（3.2 常规供电版，合封 IO 漏电）；[[SF32LB52_Peripheral_Power]]。

## 跨系列与存储介质说明（补充裁定）
- **存储介质类型决定 PA21 是否必须用于断电**：PA21 主要给外挂 Flash 存储做电源控制。若外挂 **Nor Flash**，其自身可进 **Deep Power Down（≈1µA）**，**可常供电、不必用 PA21 断电**；若外挂 **SPI Nand / SD Nand Flash**，自身无深度掉电机制，**必须用 PA21（或等效 GPIO）控制供电**才能低功耗。本规则（PA21 控制 VDD_SIP 防 hibernate 漏电）对 Nand/SD Nand 场景及需断电场景适用。
- **电池系列（SF32LB52x）替代方案**：无 PA21，外挂存储供电控制改选 **PA11（MPI2_VDD_EN/SD_VDD_EN，默认 PU）** 驱动电源开关使能（复位/启动早期维持确定电平，避免误上电或漏电；参考设计黄金样板见 [[SF32LB52x_batt_Reference_Schematic]]）。详见 [[SF32LB52_Peripheral_Memory]] §4.1、[[CR_RefDesign_ExternalFlash_Power]]。

## 关联页面
- 电源：[[SF32LB52_Peripheral_Power]]｜设计规范：[[DR_LowPower_IO_Retention]]、[[DR_PowerArchitecture]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P42（§3.2，避免合封 IO 漏电）

## 待核实问题
- 无。
