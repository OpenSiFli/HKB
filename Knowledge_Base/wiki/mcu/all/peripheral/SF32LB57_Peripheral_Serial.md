---
title: SF32LB57 串行通信外设（UART / I2C / SPI / CAN）
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Serial","SF32LB57串口","SF32LB57 UART","SF32LB57 I2C","SF32LB57 SPI","SF32LB57 CAN"]
tags: ["企业MCU","外设-串口","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 串行外设资源：**3× UART、4× I2C、2× SPI（SSP）、2× CAN、1× USB2.0 FS**，另有 **2× I2S、2× PDM**（见 [[SF32LB57_Peripheral_Audio]]）。**两系列一致**。

## 1. 资源与速率（Table 3-1）
| 控制器 | 数量 | 最高速率 | 备注 |
|---|---|---|---|
| UART | 3 | **3 Mbaud** | 通用异步收发器 |
| I2C | 4 | **3.4 MHz** | |
| SPI | 2 | **48 MHz** | 支持 SSP / SPI / Microwire 帧格式 |
| CAN | 2 | **1 Mbps** | **CAN 2.0b，不支持 CAN FD** |
| USB | 1 | USB2.0 FS | 见 [[SF32LB57_Peripheral_USB]] |
| I2S | 2 | 48 kHz 采样（48kHz×32bit×2ch） | |
| PDM | 2 | 3.072 MHz | |

## 2. CAN 主要特性（§3.9）
- 兼容 **CAN 2.0b**，**不支持 CAN FD**
- 可配置数据率至 **1 Mbps**
- 支持基础帧与扩展帧；帧数据长度可达 **8 byte**
- 接收 FIFO 深度 **7**，发送 FIFO 深度 **7+1**
- **16 个**灵活可配置的 ID 过滤器，仅在接收 FIFO 中保存过滤后的帧
- 支持多帧自动收发、自动重传、**帧抢占发送**
- 完备的错误检测与通知机制
- ⚠️ CAN 需外接 CAN 收发器（本芯片为 CAN 控制器）

## 3. SPI 帧格式（§3.5.6）
支持 **SSP / SPI / Microwire** 三种帧格式；SPI 时序含 SPH=0 与 SPH=1 两种（图 3-6 / 3-7）。

## 4. 硬件设计约束
- **I2C 总线须外加上拉电阻**（本册未给出具体阻值；SF32LB52 家族参考设计为 7.5kΩ / eMMC-SD 场景，**不可直接套用**，待补 57 家族参考设计）。总线电容与从器件数量须满足 I2C 规范。
- **UART** 电平须与对端匹配；3.3V 系列由 VDDIOA 决定，电池系列由内部 IO 域决定（见 [[SF32LB57_Peripheral_GPIO]]）。
- **SPI** 走线尽量短，高速（≤48MHz）时注意阻抗与串扰，避免与射频/天线平行走线。
- **CAN** 须外接 CAN 收发器，CANH/CANL 走差分对并做 120Ω 终端匹配（按节点拓扑）。
- 所有串行接口电平域须与外设一致，跨压域须加电平转换。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- GPIO/复用：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Pinmux]]
- USB：[[SF32LB57_Peripheral_USB]]｜存储：[[SF32LB57_Peripheral_Memory]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Table 3-1（P38）、§3.5.2 UART（P16）、§3.5.3 I2C（P17）、§3.5.6 SPI（P18）、§3.9 CAN（P38）。
2. [DS5701-SF32LB57x V0.2]，同上（P38–39 等）。

## 待核实问题
1. 各 UART / I2C / SPI / CAN 实例对应的 GPIO 复用引脚，待补 Pinmux / 用户手册。
2. I2C 上拉电阻推荐值本册未给出，禁止套用 SF32LB52 的 7.5kΩ，待官方参考设计。
3. 是否存在仅用于调试（如蓝牙 HCI）而应用不可用的串口实例（SF32LB52 家族有此情况），本册未说明，待补用户手册。
