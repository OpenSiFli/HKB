---
title: FC-SDMMC FIFO溢出
type: mcu_fault
aliases: ["FC_SDMMC_FIFO_Overflow","SDMMC FIFO溢出故障"]
tags: ["企业MCU","故障案例","根因分析","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Peripheral_Memory]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 一般
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
SF32LB52X SDMMC 内置 2KB FIFO 在大数据量传输时若 DMAC 另一端存储堵塞，会 overflow/underflow 导致传输出错，本文给出根因与规避。

## 核心硬件内容（背景）
- 故障所属电路模块：存储接口（SDMMC）。
- 相关芯片与硬件版本：SF32LB52X 全型号（SDMMC 与 MPI2 复用 PA12~PA17），用户手册 V0.8.8（§14.1.3）。

## 专项业务内容 —— 故障复盘（必填）
1. **失效现象、复现条件**：SD/eMMC 读写出错或卡顿；多块传输、总线带宽紧张或 DMAC 另一端存储堵塞时出现。
2. **涉及 MCU 型号、硬件版本**：SF32LB52X 家族（QFN68L），手册 V0.8.8。
3. **根因硬件分析**：SDMMC 内置 2KB FIFO 缓存读写数据；若 DMAC 搬运另一端存储堵塞、未及时响应 FIFO 请求，FIFO 上溢/下溢产生 SR_FIFO_OVERRUN/UNDERRUN 并记录/中断，数据传输出错。另 SDMMC 与 MPI2 复用 PA12~PA17，冲突使用会致外部 Flash 或 SD 不可访问。
4. **短期整改方案、长期设计规避规则**：
   - 设 CLKCR_VOID_FIFO_ERROR 在 FIFO 不足时自动停 CLK 防错误；保证 DMAC 带宽；多块传输确保 DLR_DATA_LEN 为块尺寸整数倍。
   - 原理图/固件避免 SDMMC 与 MPI2 同时启用（见 [[CR_SDMMC_MPI2_Exclusive]]）。
5. **同类图纸审图拦截规则**：对应 [[CR_SDMMC_MPI2_Exclusive]]（SDMMC 与 MPI2 引脚互斥）。

## 关联页面
- 存储接口外设：[[SF32LB52_Peripheral_Memory]]｜芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 校验规则：[[CR_SDMMC_MPI2_Exclusive]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P341–P342（§14.1.3，FIFO 管理）

## 待核实问题
- 无。
