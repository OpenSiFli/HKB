---
title: DR-BOOT模式设计规范(SF32LB52X)
type: mcu_design_rule
aliases: ["DR_BootMode","SF32LB52X BOOT设计规范"]
tags: ["企业MCU","通用设计规范","BOOT/启动","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
created: 2026-08-11
updated: 2026-08-13
---

## 摘要
SF32LB52X BOOT 模式由 HPSYS_CFG BMR 寄存器 Bit0（**ROM 启动流程标志位**）决定（0=正常/加载用户程序，1=下载），本规范指导量产/产测的启动模式设计，避免误入下载模式或启动失败。注：BMR[0] 与 PA13/PA17 等存储接口引脚无关（见下方特别说明）。

## 核心硬件内容
### 1. 规范主题与适用范围
- 主题：芯片启动模式配置、下载/产测入口、固件自启动保证。
- 适用：全部 SF32LB52X 产品启动设计。

### 2. 设计要求
- BOOT 模式由 **HPSYS_CFG BMR 寄存器 Bit0** 决定：0=正常模式，1=下载模式（专用 boot mode 地址 0xFFA57200）。
- HPSYS_CFG IDR：SID=0xC2、CID=0x04、Package ID、REVID；SYSCR：LDO_VSEL（0=增强/1=基础模式）、SDNAND、WDT1_REBOOT。
- 量产固件确保 BMR[0]=0（正常模式）；下载/产测通过调试接口或受控 strapping 进入下载模式。
- 在图纸与 BOM 注明 BOOT 逻辑，便于产测/返修。

### 3. 约束禁忌
- 误置 BMR[0]=1 → 固件不运行、设备"变砖"（严重）。
- BOOT 外部 strapping 与寄存器 BMR 配置矛盾 → 启动不确定性。

### 4. 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §5.7（P91，HPSYS_CFG BMR）；[[SF32LB52x_batt|SF32LB52x]] §8。

## 特别说明 —— PA13/PA17 与 BMR[0] 无关
- **BMR[0] 是 ROM 中的启动流程标志位**（HPSYS_CFG BMR Bit0），决定上电启动流程：是否加载用户程序、是否进入下载模式等（参考用户手册 §5.7 / §8），不依赖外部引脚。
- **PA13 / PA17 与 BMR[0] 无关**：二者是 SDMMC/MPI2 存储接口引脚（SD_D3/SD_D1），仅用于**从外部存储启动时判别存储类型**，不属于 BOOT 模式寄存器配置。AI 审图勿将存储接口异常误判为 BOOT/BMR 问题。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜调试接口：[[DR_Debug_Interface]]
- 校验规则：[[CR_BootMode_Register]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P91（HPSYS_CFG 寄存器映射表）

## 待核实问题
- BOOT 外部 strapping 电路图手册未给出，若设计依赖外部 BOOT 引脚需补参考设计核实。
