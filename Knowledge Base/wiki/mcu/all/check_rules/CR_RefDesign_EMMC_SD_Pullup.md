---
title: CR-参考设计-eMMC/SD Nand上拉电阻
type: mcu_check_rule
aliases: ["CR_RefDesign_EMMC_SD_Pullup","eMMC上拉审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_3V3_Reference_Schematic],[SF32LB52x_batt_Reference_Schematic],[SF32LB52_Peripheral_Memory]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52 官方参考设计，校验 **eMMC / SD Nand Flash 接口的上拉电阻**是否齐备：PA13(SD_D3)、PA15(SD_CMD)、PA17(SD_D1) 均须加 **7.5KΩ 上拉**（参考位号 R0101 / R0160 / R0102）。

## 核心硬件内容（背景）
- eMMC 与 SD Nand 走 MPI2/SDMMC 接口，CMD 与 D3 等信号在初始化阶段需确定电平，必须外部上拉。
- 参考设计明确规定：eMMC 须焊接 R0102(PA17)、R0101(PA13)、R0160(PA15)；SD Nand 须焊接 R0101(PA13)、R0160(PA15) 共 **7.5KΩ** 上拉。
- 与 [[CR_SDMMC_MPI2_Exclusive]]（MPI2/SDMMC 互斥使用）互补：本条专管上拉硬件。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到 eMMC 或 SD Nand Flash 连接 PA13/PA15/PA17（SD_D3/SD_CMD/SD_D1）时触发。
2. **违规现象描述**：PA13/PA15/PA17 上对应上拉电阻缺失或阻值非 7.5KΩ（如 DNP、悬空）→ eMMC/SD Nand 初始化失败、无法枚举。
3. **风险影响说明**：上拉缺失 → 存储不识别/枚举失败/偶发掉卡（严重）。
4. **标准化整改方案**：在 PA13、PA15、PA17 到电源（与 VDDIOA 同压）各加 **7.5KΩ** 上拉（eMMC 三处全加；SD Nand 加 PA13/PA15）。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_Memory]]；参考设计两页（eMMC/SD Nand 上拉要求）。

## 关联页面
- 存储外设：[[SF32LB52_Peripheral_Memory]]｜互斥规则：[[CR_SDMMC_MPI2_Exclusive]]｜接口电平：[[CR_RefDesign_Interface_VoltageMatch]]

## 原始来源完整引用
1. [SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf] / [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/，设计注释（eMMC：R0102/R0101/R0160；SD Nand：R0101/R0160，均 7.5K）

## 待核实问题
- 无（参数来自参考设计黄金样板）。
