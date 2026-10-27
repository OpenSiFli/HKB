---
title: SF32LB52 外设-串口(UART/I2C/SPI)
type: mcu_periph
aliases: ["SF32LB52X UART","SF32LB52X I2C","SF32LB52X SPI","SF32LB52X Serial"]
tags: ["企业MCU","外设模块-UART/I2C/SPI","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52x_Datasheet_V0.2.6],[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Datasheet_V2.5.5]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
series_applicability: ["通用-两系列共用"]
created: 2026-08-10
updated: 2026-08-12
---

## 摘要

> **适用系列**：本外设为 SF32LB52X（电池供电）与 SF32LB52x（3.3V 供电）两系列**共用**；两系列外设逻辑一致，差异仅在电源架构与电源专用引脚（见 [[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_GPIO]]）。
SF32LB52 串行通信外设：**应用开发可用的 UART 为 3 个（UART1/2/3，均位于 HPSYS，最高 3Mbps）**；规格书另列的 **UART4/5 位于 LPSYS，实为蓝牙 HCI 调试专用接口**，正常应用开发不可使用，**不计入可用 UART 资源**。I2C×4（主从，最高 3.4Mbps HS）、SPI×2（SPI1/SPI2，最高 48MHz，8~32bit，主从/SSP/Microwire）。本页整理三者的引脚映射、电平与时序电路约束。**⚠️ 串口资源以本页口径为准：可用 UART = UART1/2/3（HPSYS），UART4/5 仅供蓝牙 HCI 调试。**

## 核心硬件内容
### 1. UART（§3.5.2，P16）
- **实例划分（应用开发口径）**：
  - **HPSYS（大核）提供 UART1 / UART2 / UART3 共 3 个**，供用户应用开发使用（最高 3Mbps）。引脚分布在 PA_I2C_UART 复用组（Sel#=4），具体 TX/RX/CTS/RTS 由 PINMUX 在 HPSYS_CFG 中分配。
  - **LPSYS（小核）的 UART4 / UART5 为蓝牙 HCI 调试专用接口**：专供片内蓝牙协议栈与调试器通信，**应用层不可将其当作通用 UART 使用**，不占用用户可用串口资源。
- 全双工异步，16/8 倍过采样；数据位 7/8/9、停止位 1/2；硬件流控 CTS/RTS；DMA。
- 引脚：UART1/2/3 分布在 PA_I2C_UART 复用组（Sel#=4），具体 TX/RX/CTS/RTS 由 PINMUX 分配（datasheet 文本未列逐引脚 UART 映射，待核实）。
- 电平：IO 跟随 VDDIOA（见 GPIO 页）。

### 2. I2C（§3.5.3，P16–P17）
- 主/从，8 字节 FIFO，标准/快速/快速+/高速（最高 3.4Mbps）；7/10 位地址；时钟拉伸；DMA。
- 开漏总线须外部上拉电阻（阻值按总线电容与速率计算）；复用组 PA_I2C_UART（Sel#=4）。

### 3. SPI（§3.5.6，P17–P19）
- SPI1/SPI2，CLK 最高 48MHz（HPSYS）；数据宽度 8~32bit；SPO/SPH 可配；片选极性可配；FIFO 可调；DMA。
- 引脚：SPI1 = PA24(DIO)/PA25(DI)/PA28(CLK)/PA29(CS)；SPI2 = PA37(DIO)/PA38(DI)/PA39(CLK)/PA40(CS)（Sel#=2）。

### 4. 约束禁忌
- I2C 必须外部上拉，禁止直连无上拉导致总线无法释放。
- SPI 片选（CS）在多设备共享时须独立控制，避免总线冲突。
- 高速 SPI/I2C 走线注意阻抗与串扰；UART 流控在高速下建议使能以保可靠。

### 5. 规范依据
- Datasheet §3.5.2~§3.5.6（P16–P19）、Table 3-1 接口速率（P28）、Table 5-2（SPI1/SPI2 引脚，P53–P56）

## 用户手册 V0.8.8 补充（I2C 总线恢复 / 调试串口）
来源：[[SF32LB52X_UserManual_V0.8.8]] §7.1.3.12（P138）、§15.8（P362）。

- **I2C 总线卡死恢复**（7.1.3.12）：电气干扰/设备异常会导致 I2C 卡死（收发持续失败）。恢复：①复位 I2C 模块（CR_UR 置1 等 100us 后置0）；②若 BMR_SCL/BMR_SDA 均为1，置 CR_RSTREQ 由 I2C 发送 RCCR_RSTCYC 个时钟周期尝试恢复；③若 SCL/SDA 持续为0，怀疑上拉失效或从设备挂死，需检查硬件电路或复位从设备。详见 [[FC_I2C_BusStuck]]。
- **USART1 调试默认配置**：芯片启动后 USART1 默认开启，RX=PA18、TX=PA19，默认 **1M 波特、8 数据、1 停止、无校验**，监听自定义调试帧并自动调用 DMAC1 专用通道。固件若改了波特率/端口映射，调试须按新配置连接。详见 [[DR_Debug_Interface]]、[[FC_DebugInterface_Failure]]。
- I2C 开漏总线外部上拉不可省略（原约束保留）。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设 UART/I2C/SPI 引脚映射、速率、I2C 总线恢复等硬件约束在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜电源：[[SF32LB52_Peripheral_Power]]
- 校验规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.5.2~§3.5.6（P16–P19）、Table 3-1（P28）、Table 5-2（P53–P56）

## 待核实问题
- UART1-3（HPSYS，应用可用）与各 GPIO 的逐引脚 TX/RX/CTS/RTS 映射表 datasheet 文本未显式列出，待补 PINMUX 章节/参考设计。
- UART4/5（LPSYS）为蓝牙 HCI 调试接口，其引脚与使能方式以蓝牙协议栈/调试工具链为准，不纳入应用串口规划。
