---
title: SF32LB52 外设-音频模拟
type: mcu_periph
aliases: ["SF32LB52X Audio","SF32LB52X DAC","SF32LB52X Audio ADC"]
tags: ["企业MCU","外设模块-音频","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
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
SF32LB52X 集成高保真音频：24-bit Audio DAC（DACP/DACN 差分输出，SNR 109dB）与 24-bit Audio ADC（ADCP 输入，SNR 99dB），并提供 MIC_BIAS（引脚40，1.4~2.8V/0~2mA）与 AUD_VREF（引脚39）。本页整理音频模拟前端电路约束。

## 核心硬件内容
### 1. 工作机制（§3.2.3~§3.2.5，P13–P14）
- Audio DAC：24-bit，采样 8k~48kHz，差分输出 DACP(37)/DACN(36)，支持数字音量 192 级、零交叉检测。
- Audio ADC：24-bit，采样 8k~48kHz，输入 ADCP(41)，支持单端/全差分麦克风，数字高通滤除 DC；每 ADC 独立增益。
- AUDPRC 完成采样率转换/混音/均衡（DAC 路径 2ch、ADC 路径 2ch）。

### V2.5.5 实测音频指标（Table 4-16 Audio ADC / 4-17 Audio DAC，P37）
| 指标 | Audio DAC | Audio ADC | 单位 / 条件 |
|------|-----------|-----------|-------------|
| 分辨率 | 24 | 24 | Bits |
| 输出摆幅 / 采样率 | 1.1 Vrms / 8~48k | — / 8~48k | Vrms / kHz |
| 动态范围 DR | 109 | 99 | dB（A‑加权，‑60dBFS） |
| 信噪比 SNR | 109 | — | dB（A‑加权，0dBFS） |
| 总谐波失真+噪声 THD+N | ‑102 | ‑76 | dB |
| 本底噪声 | 3.7 | — | µV rms |
| 模拟增益范围（ADC） | — | ‑6~18（6dB/step） | dB |
| 输入电阻（ADC, 0dB） | — | 23 | kΩ |

> V2.5.5 给出上述实测值，较 V0.2.6 仅「SNR 109dB(DAC)/99dB(ADC)」概要更完整；电源干净度（AVDD33_AUD 隔离滤波）是达成该指标的前提。

### 2. 标准电路要求
- **电源**：AVDD33_AUD（引脚 38）2.97~3.63V，独立低噪声滤波去耦（音频敏感）。
- **参考电压 AUD_VREF（39，A,I）**：稳定参考，须去耦。
- **MIC_BIAS（40，PWR）**：输出 1.4~2.8V、0~2mA，供驻极体/数字麦克风偏置；负载电流不可超限。
- **DAC 输出（DACP/DACN 37/36）**：差分驱动，负载典型 10kΩ（特性测试条件）；按耳机/线路要求设计。
- ADC 输入 ADCP（41）支持单端/差分麦克风。

### 3. 约束禁忌
- AVDD33_AUD 必须与数字电源隔离滤波，否则 SNR 劣化（DAC SNR 109dB / ADC 99dB 依赖干净电源）。
- MIC_BIAS 负载电流严禁超过 2mA，电压不超 2.8V。
- 音频走线远离数字/RF，做好屏蔽与地分割。

### 4. 规范依据
- Datasheet §3.2.3~§3.2.5（P13–P14）、§4.4 Audio Characteristics Table 4-17/4-18（P36）、Table 5-3（ADCP41/MIC_BIAS40/AUD_VREF39/DACP37/DACN36/AVDD33_AUD38，P47）

## 用户手册 V0.8.8 补充（PDM 麦克风 / Audcodec）
来源：[[SF32LB52X_UserManual_V0.8.8]] §11（P277–P307）。

- **PDM 数字麦克风典型连接（P277）**：一对数字麦克风可共用同一比特流时钟 PDM1_CLK 与数据线，借助麦克风 L/R 配置引脚，一个在 CLK 上升沿、另一个在下降沿提供有效数据。
- **PDM 时钟**：源可选 48MHz 晶振（内部 5 分频得 9.6MHz）或 Audio PLL 经 16 分频；最终 pdm_clko 经可配分频送出；支持时钟率 0.768~3.072MHz、PCM 率 8k~48kHz（表 11-1）。
- **Audcodec 供电/时钟（P307）**：供电模块给 Audio PLL/DAC/ADC/Mic 供电，bandgap 须先启动；时钟可选 XTAL48M 或 Audio PLL（后者支持 48k 以下任意采样率）。DAC 输出目标可选 Codec(24bit 立体声)/I2S(16bit)/Audprc Tx_out；ADC 源可选 Codec 或 I2S。
- MIC_BIAS(40) 默认关闭，需软件开启调压（见电源页）。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 电源：[[SF32LB52_Peripheral_Power]]｜I2S/PDM：[[SF32LB52_Peripheral_I2S_PDM]]
- 校验规则：[[CR_AbsMaxRatings]]、[[CR_PowerDomains]]、[[CR_Audio_ADC_Input]]（音频 ADC 输入：单端/差分隔直、输入范围与增益、IO 耐压、共地）

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.2.3~§3.2.5（P13–P14）、Table 4-17/4-18（P36）、Table 5-3（P47）
2. [DS5201-SF32LB52x-Datasheet V2p5p5.pdf]，Raw：raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf，Table 4-16 Audio ADC / 4-17 Audio DAC（P37）

## 待核实问题
- AUD_VREF、MIC_BIAS 外围去耦/滤波具体推荐值待补参考设计。
