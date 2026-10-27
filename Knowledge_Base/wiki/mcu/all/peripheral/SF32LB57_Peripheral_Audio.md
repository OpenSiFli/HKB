---
title: SF32LB57 音频外设（AUDPRC / DAC / ADC / PDM / I2S）
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Audio","SF32LB57音频","SF32LB57 AUDPRC"]
tags: ["企业MCU","外设-音频","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 集成音频处理模块 **AUDPRC**：**1× 24-bit 高保真 DAC**、**2× 24-bit 高保真 ADC**、**2× I2S**、**2× PDM**、音频 PLL、Micbias LDO。支持蓝牙通话与耳机 MP3 播放。**两系列音频资源与引脚一致**。

## 1. 主要特性
- **DAC**：1× 高保真 24-bit
  - Noise floor：**3.7 µVrms**
  - SNR（10kΩ 负载，A-Weighted）：**109 dB**
  - 输出摆幅：**1.1 Vrms**
  - 采样率：8 / 16 / 11.025 / 22.05 / 24 / 32 / 44.1 / 48 / 88.2 / 96 kHz
  - 支持 **192 级数字音量**，带**过零检测**
- **ADC**：2× 高保真 24-bit
  - SNR（A-Weighted）：**97 dB**
  - 输入电阻：23 kΩ（Gain=0dB @48kHz）
  - 模拟增益范围：‑6 ~ +18 dB（6 dB/步进）
  - THD+N：**‑86 dB**
  - 采样率：8 / 11.025 / 12 / 16 / 22.05 / 24 / 32 / 44.1 / 48 / 88.2 / 96 kHz
  - 数字高通滤波器（消除 ADC 直流偏置）；支持**单端与全差分麦克风输入**
- **Micbias LDO**：输出 **1.4 ~ 2.8 V**，输出电流 **0 ~ 2 mA**
- **数字音频接口**：**2× I2S**（48kHz 采样，48kHz×32-bit×2ch）、**2× PDM**（3.072 MHz）
- 音频 PLL（AUDPRC PLL）

## 2. 音频引脚（两系列一致，QFN68）
| 引脚 | 名称 | 类型 | 说明 |
|---|---|---|---|
| 38 | AVDD33_AUD | PWR | 音频电源输入，**接 3.3V 电源** |
| 39 | AUD_VREF | A,I | 音频参考电压输入，**接电容到地，不用外供电源** |
| 37 | DACP | A,O | 音频 DAC 输出（P） |
| 36 | DACN | A,O | 音频 DAC 输出（N） |

**QFN80（3.3V 系列）**：AVDD33_AUD=22、AUD_VREF=23、DACP=21、DACN=20。
> ⚠️ 麦克风输入（MIC）与 Micbias 的具体引脚号本册 Table 5-3 未单列，待补。

## 3. 硬件设计约束
- **AVDD33_AUD(38) 必须接 3.3V 电源**；**AUD_VREF(39) 接电容到地，禁止外供电源**。
- **DACP(37)/DACN(36)** 为差分输出，走线须等长、远离射频与数字开关噪声；外接负载 ≥10kΩ 方可达到标称 SNR/DR。
- **Micbias** 输出电流能力仅 0~2mA，设计驻极体/MEMS 麦克风偏置时不得超载。
- 音频模拟走线与 BRF_ANT/BUCK_LX 等高噪声源保持间距，必要时包地。
- 使用全差分麦克风时按规格书要求连接 ADC 差分输入对。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 电源：[[SF32LB57_Peripheral_Power]]｜串口：[[SF32LB57_Peripheral_Serial]]
- 音频 ADC 输入审图规则：[[CR_Audio_ADC_Input]]（单端/差分隔直、输入范围与增益、IO 耐压、共地）
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，产品特性音频段（P4）、Table 4-18 音频 ADC 性能（P47）、Table 4-19 音频 DAC 性能（P48）、Table 3-1（P38，I2S/PDM 速率）、Table 5-3（P61）。
2. [DS5701-SF32LB57x V0.2]，同上（P4 / P48–49 / P38 / P62）。

## 待核实问题
1. 麦克风输入（MIC_x）与 Micbias 的具体引脚号未在 Table 5-3 中单列，待补。
2. I2S / PDM 信号对应的 GPIO 复用引脚，待补 Pinmux / 用户手册。
3. AUDPRC 内部通路（DAC/ADC 通路）详细框图见规格书 §3.4，本次未展开。
