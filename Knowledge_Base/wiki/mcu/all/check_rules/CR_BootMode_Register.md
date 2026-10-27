---
title: CR-BOOT模式寄存器配置
type: mcu_check_rule
aliases: ["CR_BootMode_Register","BOOT模式审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 严重
created: 2026-08-11
updated: 2026-08-13
---

## 摘要
校验 SF32LB52X BOOT 模式配置，避免量产固件误进入下载模式或启动失败。BOOT 模式由 HPSYS_CFG **BMR 寄存器 Bit0（ROM 启动流程标志位）** 决定（0=正常模式/加载用户程序，1=下载模式），专用 boot mode 地址 0xFFA57200。注：BMR[0] 与 PA13/PA17 等存储接口引脚无关（见下方特别说明）。

## 核心硬件内容（背景）
本芯片 BOOT 主要为**寄存器配置**而非纯外部引脚 strapping。HPSYS_CFG IDR 含 SID=0xC2、CID=0x04、Package ID、REVID；SYSCR 含 LDO_VSEL（0=增强/1=基础模式）、SDNAND、WDT1_REBOOT。误置 BMR[0]=1 会进入下载模式，固件无法自启动。详见 [[DR_BootMode]]、[[SF32LB52x_batt|SF32LB52x]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 SF32LB52X 的 BOOT 相关电路（BOOT 引脚/调试接口/nRST）或固件启动配置时，核对 BOOT 模式来源与设计意图一致。
2. **违规现象描述**：① 量产板将 BOOT 强制拉高（下载模式）且无切换机制；② 调试/下载电路与正常运行模式冲突；③ 原理图标注的 BOOT 引脚 strapping 与寄存器 BMR 配置矛盾。
3. **风险影响说明**：误入下载模式 → 固件不运行、设备"变砖"；配置矛盾 → 启动不确定性、产测/返修困难（严重）。
4. **标准化整改方案**：量产固件确保 BMR[0]=0（正常模式）；下载/产测通过调试接口或受控 strapping 进入；在图纸与 BOM 注明 BOOT 逻辑。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P91（HPSYS_CFG BMR）；[[SF32LB52x_batt|SF32LB52x]] §8 BOOT。

## 特别说明 —— PA13/PA17 与 BMR[0] 无关
- **BMR[0] 是 ROM 中的启动流程标志位**（HPSYS_CFG BMR Bit0）。它决定上电后的启动流程走向：是否加载并运行用户程序、**是否进入下载模式**等（详见 [[SF32LB52X_UserManual_V0.8.8]] §5.7 / §8）。BMR[0] 由固件/寄存器配置决定，**不依赖任何外部引脚电平**。
- **PA13 / PA17 与 BMR[0] 完全无关**。PA13（SD_D3）、PA17（SD_D1）是 SDMMC/MPI2 存储接口引脚，仅在**从外部存储启动**时用于**判别存储类型**（区分 NOR / NAND / SD 等不同存储介质），属于存储启动识别逻辑，不属于 BOOT 模式寄存器配置。
- → **AI 审图注意**：不要将「PA13/PA17 上拉缺失 / 连接异常」误判为 BOOT/BMR 配置问题；存储接口（PA12~PA17）与启动模式寄存器（BMR[0]）是两个独立维度，详见 [[CR_SDMMC_MPI2_Exclusive]]、[[CR_RefDesign_EMMC_SD_Pullup]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜设计规范：[[DR_BootMode]]｜报告模板：[[index_MCU_ALL]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P91（HPSYS_CFG 寄存器映射表，BMR Bit0）

## 待核实问题
- BOOT 外部 strapping 电路图手册未给出；若设计依赖外部 BOOT 引脚，需补 SiFli 参考设计核实。
