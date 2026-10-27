---
title: SF32LB52 外设-USB2.0 FS
type: mcu_periph
aliases: ["SF32LB52X USB","SF32LB52X USB2.0 FS"]
tags: ["企业MCU","外设模块-USB","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
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
SF32LB52X 集成全速（FS）USB2.0 Host/Device 接口，片内集成 USB2.0 FS PHY，差分数据线 DP/DM 映射到 GPIO PA35(#USB11_DP) / PA36(#USB11_DM)。本页整理 USB 引脚、片内 PHY 与布线约束。

## 核心硬件内容
### 1. 工作机制
- USB2.0 FS（12Mbps），软件可配端点、支持 suspend/resume、动态 FIFO、SRP/HNP、全速/低速模式。
- DP/DM：PA35 = #USB11_DP，PA36 = #USB11_DM（复用 Sel#=2）。

### 2. 标准电路要求
- **片内 PHY**：无需外置 USB 收发器；DP/DM 直接引出，按 USB FS 规范做 90Ω（差分）±10% 阻抗控制。
- 需外接 VBUS 检测与必要的上拉/下拉（FS 上行设备 D+ 1.5kΩ 上拉，由控制器/外部实现）。
- DP/DM 走线做差分等长、远离噪声源、适当包地。

### 3. 约束禁忌
- 禁止在 DP/DM 上外接独立 USB 收发器（片内已集成）。
- 差分阻抗与等长不满足将引起眼图劣化/通信失败。
- DP/DM 引脚（PA35/PA36）复用须确认 Sel#=2，且未被 GPIO 或其他功能占用。

### 4. 规范依据
- Datasheet §3.5.8 USB2.0 FS（P20）、Table 5-2（PA35/PA36，P55）、§1.3.3 存储器映射 USBC 0x5004_7000

## 用户手册 V0.8.8 补充（UART 调试接口）
来源：[[SF32LB52X_UserManual_V0.8.8]] §15.7–15.10（P341–P363）。

- 除片内 USB PHY 外，本芯片提供 **UART 调试接口**：经 USART1（RX=PA18、TX=PA19），上电默认开启，默认 **1M 波特、8 数据、1 停止、无校验**，监听自定义调试帧并自动经 DMAC1 专用通道读写总线。可通过地址 0xF0000000~0xFFFFFFFF 访问 HCPU 系统寄存器实现暂停/状态/单步/系统复位等。
- **调试失效原因（15.9）**：波特率错误（固件改了 USART1 波特率）、USART1 端口重映射、DMAC1 时钟关闭/复位、DMAC1 总线卡死（MPI 未初始化时访问其存储空间）、HPSYS 进入低功耗（deepsleep/standby/hibernate）、EFUSE 禁用调试。详见 [[DR_Debug_Interface]]、[[CR_DebugInterface_PA18_PA19]]、[[FC_DebugInterface_Failure]]。
- USB DP/DM 片内 PHY 约束（原 §3.5.8 保留，见 [[CR_USB_DPDM]]）。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设 USB2.0 FS 接口、片内 PHY、DP/DM 引脚映射、UART 调试接口在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜电源：[[SF32LB52_Peripheral_Power]]
- 校验规则：[[CR_USB_DPDM]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.5.8（P20）、Table 5-2（P55）

## 待核实问题
- VBUS 检测电路、FS 上拉电阻实现方式待补参考设计。
