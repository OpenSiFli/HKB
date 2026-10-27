---
title: CR-SDMMC与MPI2引脚互斥(PA12~PA17)
type: mcu_check_rule
aliases: ["CR_SDMMC_MPI2_Exclusive","SDMMC/MPI2互斥审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Memory]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 严重
created: 2026-08-11
updated: 2026-08-13
---

## 摘要
校验 SF32LB52X 的 SDMMC 与 MPI2 共用引脚 PA12~PA17，在原理图/固件中不冲突启用，避免外部 Flash 不可访问或 SD 失效。

## 核心硬件内容（背景）
SDMMC 与 MPI2 使用相同 IO（PA12~PA17），因此使用 SDMMC 功能时**不能**通过 MPI2 访问外部 Flash。二者互斥。详见 [[SF32LB52_Peripheral_Memory]] §14、[[FC_SDMMC_FIFO_Overflow]]。

> **与 BOOT 的关系**：PA12~PA17（含 PA13/PA17）仅在**从外部存储启动**时用于**判别存储类型**（区分 NOR/NAND/SD 等），属存储启动识别逻辑；该引脚组与 BMR[0]（ROM 启动流程标志位）**完全无关**，AI 审图勿将存储接口问题误判为 BOOT/BMR 配置问题。见 [[CR_BootMode_Register]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 PA12~PA17 同时连接外部 Flash（MPI2/QSPI）与 SD 卡座（SDMMC）时，核对设计是否允许二者同时工作。
2. **违规现象描述**：① 同一组 PA12~PA17 既接外 Flash 又接 SD，且固件需同时访问；② 复用冲突导致 XIP/外部存储或 SD 功能二选一却未做地址/片选隔离；③ 误将 SiP 存储与外部 MPI2 地址冲突。
3. **风险影响说明**：引脚冲突 → 外部 Flash 不可访问（固件跑飞）或 SD 功能失效（严重）。
4. **标准化整改方案**：明确二选一或分时复用；若必须共存，通过不同 IO 组走线（MPI2 另选可用引脚）或硬件开关；固件避免同时使能 SDMMC 与 MPI2。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P339（14.1 简介）；[[SF32LB52_Peripheral_Memory]]。

## 关联页面
- 存储接口：[[SF32LB52_Peripheral_Memory]]｜故障案例：[[FC_SDMMC_FIFO_Overflow]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P339（§14.1 简介）

## 待核实问题
- 无。
