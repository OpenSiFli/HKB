---
title: SF32LB52 外设-I2S与PDM
type: mcu_periph
aliases: ["SF32LB52X I2S","SF32LB52X PDM","SF32LB52X 音频接口"]
tags: ["企业MCU","外设模块-I2S/PDM","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
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
SF32LB52X 数字音频接口：I2S1（主/从、全双工、最高 24-bit、采样 48kHz）与 PDM1（PDM 麦克风接口，多时钟率/多 PCM 率）。本页整理二者引脚映射与电路约束（常与 Audio 模拟前端配合使用）。

## 核心硬件内容
### 1. I2S（§3.5.5，P17）
- 主/从、全双工；左/右对齐与标准格式；8/16-bit 单/立体声、位宽最高 24-bit。
- 引脚（复用组，见 GPIO 页）：I2S1_MCLK（PA02/PA24）、I2S1_SDO（PA03/PA25）、I2S1_SDI（PA04/PA28）、I2S1_BCK（PA05/PA29）、I2S1_LRCK（PA06/PA30）。Sel#=3。

### 2. PDM（§3.5.4，P17）
- PDM→PCM 转换；支持左右声道/单声道；时钟率 0.768~3.072MHz；PCM 率 8k~48kHz；32/24/16/8-bit；增益 ‑15~45dB（0.5dB 步进）。
- 引脚：PDM1_CLK（PA07/PA22）、PDM1_DATA（PA08/PA23）。Sel#=3。

### 3. 电路要求
- I2S 为数字音频总线，注意 BCK/LRCK/数据线等长与时序；连接外部 Codec/数字麦克风。
- PDM 麦克风时钟由 PDM1_CLK 提供，DATA 单/双线；注意时钟频率与 PCM 率匹配。
- 与音频模拟前端（[[SF32LB52_Peripheral_Audio]]）协同：I2S/PDM 的数字信号最终经 AUDPRC 处理。

### 4. 约束禁忌
- I2S/PDM 引脚复用须确认 Sel#=3，避免与 LCDC1/GPIO 冲突。
- PDM 时钟频率须与所选 PCM 采样率匹配，否则采样错误。

### 5. 规范依据
- Datasheet §3.5.4~§3.5.5（P17）、Table 3-1（I2S 48kHz、PDM 3.072MHz，P28）、Table 5-2（PA02/03/04/05/06/07/08/22/23/24/25/28/29/30，P50–P53）

## 用户手册 V0.8.8 补充（PDM 时钟配置 / 双麦连接）
来源：[[SF32LB52X_UserManual_V0.8.8]] §11.1（P277–P278）。

- PDM 时钟源：系统 48MHz 晶振（PDM 内先 5 分频得 9.6MHz）或 Audio PLL 经 16 分频，二选一后再经可配分频得 pdm_clko（送给数字麦克风）。
- 输出数据率 = pdm_clko / (sinc_rate × lpf_downsample)；sinc_rate 与 lpf_ds 按表 11-1 配置（如 3.072MHz→48kHz 取 SINC RATE 32、LPF 后下采样 2、SINC ORDER 3）。
- 双数字麦克风典型连接：共用 CLK 与 DATA，借助 L/R 引脚使一芯上升沿、另一芯下降沿输出（见 [[SF32LB52_Peripheral_Audio]]）。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设 I2S/PDM 引脚映射、速率、双数字麦克风连接等硬件约束在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 音频模拟：[[SF32LB52_Peripheral_Audio]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]
- 校验规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.5.4~§3.5.5（P17）、Table 3-1（P28）、Table 5-2（P50–P53）

## 待核实问题
- I2S/PDM 与外置 Codec 的具体参考连接电路待补设计示例。
