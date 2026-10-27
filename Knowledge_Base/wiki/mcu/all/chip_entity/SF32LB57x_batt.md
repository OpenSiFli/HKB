---
title: SF32LB57x（电池供电系列）
type: mcu_chip
aliases: ["SF32LB57x 电池系列","SF32LB57x(电池供电)","SiFli SF32LB57x"]
tags: ["企业MCU","芯片系列-SF32LB57","型号-SF32LB57x 电池系列","芯片实体","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
mcu_series: ["电池供电系列"]
mcu_model: ["SF32LB573UB7N6","SF32LB573UB766","SF32LB573UB776","SF32LB575UCNN6","SF32LB575UC7N6","SF32LB577UDNN6"]
hardware_version: ["QFN68 7x7","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SiFli **SF32LB57x（小写 x）= 电池供电系列**，超低功耗多核双系统 MCU（双 Arm Cortex-M33 STAR-MC1 @240MHz / 24MHz，1968 CoreMark），集成 2D/2.5D ePicasso 3.0 图形引擎、592KB SRAM、双模蓝牙 6.3。**内置锂电充电模块**（VBUS 输入），由 **VCC 接电池**供电，并提供 **VSYS 3.0V 输出**与**两路对外 3.3V LDO（各 150mA）**。适用于智能手表/手环、可穿戴医疗、便携终端等电池供电场景。

> 同家族另有 **SF32LB57X（大写 X）= 3.3V 供电系列**（无充电、PVDD 主电），见 [[SF32LB57X]]；家族总览见 [[SF32LB57]]。
>
> 📌 **文档来源**：本系列由 **DS5701-SF32LB57x-CN**（标题小写 x）描述，与芯片命名一致。见 [[SF32LB57x_batt_Datasheet_V0.2_20260909]]。
>
> 📌 **NTFS 说明**：本页文件名带 `_batt` 后缀（Windows 不区分大小写，`SF32LB57X.md` 与 `SF32LB57x.md` 会冲突）。引用请写 `[[SF32LB57x_batt|SF32LB57x]]`。
>
> ⚠️ **本系列规格书为 V0.2 草稿**，功耗参数全部 TBD，量产前须复核。

## 核心硬件内容

### 1. 芯片基础
- 厂商 / 系列：SiFli（思澈科技）/ SF32LB57x 电池供电系列（57 家族）
- 内核：双 Arm Cortex-M33 STAR-MC1（HPSYS 双性能核）@240MHz，1968 CoreMark
  - HCPU：32KB(2-way) I$ + 16KB(4-way) D$；ACPU：16KB(2-way) I$ + 8KB(4-way) D$
  - LPSYS：Cortex-M33 STAR-MC1 @24MHz
- 存储：片上 SRAM **592KB**（HPSYS 512KB + LPSYS 80KB，全部 Retention）；SiP 合封随料号（见 §订购信息）
- 封装：**QFN68** 7×7mm（T0.9 / T1.1，P0.35）—— **订购信息（Table 6-1）仅列 QFN68 料号**；DS5701 已详述 QFN80/BGA112 管脚与封装尺寸，但 V0.2 中其料号缺失（规格书【严重】缺陷，见一致性核查报告），非硬件不支持。
- 工作温度：‑40 ~ +85 °C
- 无线：双模蓝牙 6.3（BLE Audio / LE LR）；BLE 灵敏度 ‑100dBm(1Mbps)；最大发射 17dBm(BR/BLE)、13dBm(EDR2/3)
- 电源管理：内置高效率 Buck + 低功耗 LDO + **锂电充电模块**；休眠功耗 **2.8µA@3.8V**（特性页宣称，Table 4-6 全 TBD 待核实）
- **对外供电**：**VDD33_VOUT1(22)** 与 **VDD33_VOUT2(14)**，各 **150mA**

### 2. 专用引脚（Table 5-3，QFN68 = 57xUxxx6）
| 引脚 | 名称 | 类型 | 说明 |
|---|---|---|---|
| 21 | **VBUS** | PWR | **内部充电模块的电源输入口** |
| 20 | **VBAT** | PWR | 电源输出，**接电池**；内部有 ADC 检测电池电压值 |
| 19 | **VSYS** | PWR | 电源输出 **3.0V**，外挂电容到地 |
| 24 | **VCC** | PWR | 系统电源输入，**接电池** |
| 22 | **VDD33_VOUT1** | PWR | 3.3V LDO1 输出，接电容到地，带载 **150mA** |
| 14 | **VDD33_VOUT2** | PWR | 3.3V LDO2 输出，接电容到地，带载 **150mA** |
| 23 | VDD18_VOUT | PWR | 1.8V LDO 输出，内部电源，接电容到地 |
| 18 | BUCK_LX | A,I/O | Buck 电感开关，接电感一端 |
| 17 | BUCK_FB | PWR | Buck 输出，接电感另一端并接电容到地 |
| 16 | VDD_VOUT1 | PWR | 内部 LDO1 输出，接电容到地 |
| 15 | VDD_VOUT2 | PWR | 内部 LDO2 输出，接电容到地 |
| 13 | VDD_RET | PWR | RET LDO 输出，接电容到地 |
| 12 | VDD_RTC | PWR | RTC LDO 输出，接电容到地 |
| 52 | **AVDD_BRF** | PWR | 射频电源输入，**接 VSYS** |
| 38 | AVDD33_AUD | PWR | 音频电源输入，接 3.3V 电源 |
| 68 | GPADC_VREF | A,I | GPADC VREF 输入，接电容到地，**不用外供电源** |
| 55 / 54 | XTAL48M_XI / XO | A,I / A,O | 48MHz 晶体接口 |
| 53 | BRF_ANT | A,I/O | 天线接口 |
| 39 | AUD_VREF | A,I | 音频参考电压输入，接电容到地，不用外供电源 |
| 37 / 36 | DACP / DACN | A,O | 音频 DAC 输出 |
| 69 | EPAD | GND | 散热裸焊盘，须接 GND |

> **本系列无 PVDD / VDDIOA / VBATS / AVDD33 引脚**；GPIO IO 域由内部供给（无独立 VDDIOA 外部引脚）。

### 3. 与 3.3V 系列的引脚差异（同 QFN68）
| 引脚 | 3.3V 系列 [[SF32LB57X]] | 电池系列（本页） |
|---|---|---|
| 14 | AVDD33（模拟电源输入 3.3V） | VDD33_VOUT2（3.3V LDO2 输出 150mA） |
| 19 | PVDD（PMU 电源输入 3.3V） | VSYS（电源输出 3.0V） |
| 20 | VBATS（电池电压检测输入） | VBAT（电源输出，接电池） |
| 21 | VDDIOA（GPIO 电源输入） | VBUS（充电模块电源输入） |
| 22 | NC（悬空） | VDD33_VOUT1（3.3V LDO1 输出 150mA） |
| 24 | GPIO（非专用脚） | VCC（系统电源输入，接电池） |
| 52 | AVDD_BRF（接 3.3V） | AVDD_BRF（**接 VSYS**） |

### 4. 极限电气参数（Table 4-2）
- **VBUS**：最大 **5.5 V**
- **VBAT**：最大 **4.7 V**；**VCC**：最大 **4.7 V**
- PVDD：最大 3.63 V（本系列无此引脚）
- 存储温度 Tstorage：‑40 ~ +125 °C
- ESD：**HBM ±4000V**（JS-001-2017）、**CDM ±1000V**（JS-002-2018）
- Latch-up：I-Test ±200mA、OVT +1.5×VddMAX（JESD78E）
- MSL：**MSL3**（回流 260+0°C 20s ×3）

### 5. 推荐工作条件（Table 4-1）
- **VBUS**：4.5 ~ 5 ~ 5.5 V（充电输入）
- **VBAT**：3.0 ~ 4.7 V
- **VCC**：3.0* ~ 4.7 V（* 开机电压 3.5V ±10%）
- Tamb：‑40 ~ +85 °C
- VIL ≤ 0.3×VIO；VIH ≥ 0.7×VIO；VTH ≈ 0.5×VIO

### 6. 充电模块电气特性（Table 4-20）
| 参数 | 符号 | Min | Typ | Max | 单位 |
|---|---|---|---|---|---|
| 充电输入电压 | Vbus | 4.5 | 5 | 5.5 | V |
| BAT 漏电流 | Ileak | | | 30 | nA |
| 恒流充电电流 | Icc | 5 | | 400 | mA |
| 涓流充电电流 | Itri | 0.5 | 30 | 40 | mA |
| 满电截止电流比 | Iend | | 10 | | % of Icc |
| 满电截止电压 | Vcv | 4.2 | | 4.45 | V |
| 满电电压精度 | | | | ±1.5 | % of Vcv |
| 涓流→恒流转换阈值 | Vcc | | 3 | | V |
| 复充阈值 | Vrechg | | Vcv‑0.15 | | V |
| 过充保护 | Vhigh | | | 4.78 | V |

### 7. I/O 特性（Table 4-3 @3.3V）
- CIN 2.5~3.5pF；VIH ≥0.7×VDD；VIL ≤0.3×VDD；IIH/IIL 10~40nA
- VOH ≥0.8×VDD；VOL ≤0.2×VDD
- **驱动电流 IOH/IOL：12 / 30 / 38 mA**（最大驱动强度）
- 内部上下拉 RPU/RPD：7 / 10 / 20 kΩ
- 复位：VIH_nRST ≥0.7×VDD；VIL_nRST ≤0.3×VDD
- **IO 驱动档位（Table 4-21）**：DS1/DS0 = 00→2mA、01→4mA、10→8mA、11→12mA

### 8. 最小系统要点
- **电池接 VCC(24) 与 VBAT(20)**（VBAT 同时为电池电压 ADC 检测点）。
- **VBUS(21) 为充电输入**（4.5~5.5V），充电时须满足 Table 4-20 参数。
- **VSYS(19)** 为 3.0V 输出，须**外挂电容到地**。
- **AVDD_BRF(52) 接 VSYS**（非 3.3V）。
- **VDD33_VOUT1(22) / VDD33_VOUT2(14)** 为 3.3V LDO 输出，各带载 ≤150mA，须接电容到地。
- VDD_VOUT1/2、VDD_RET、VDD_RTC、VDD18_VOUT 为内部电源输出，各接电容到地。
- GPADC_VREF(68)、AUD_VREF(39) 接电容到地，**不用外供电源**。
- 48MHz 晶体接 XTAL48M_XI(55)/XO(54)；**EPAD(69) 必须可靠接地**。
- 官方最小系统原理图见 DS5701 **P78–82**（矢量图，文本提取为反序，关键网络需人工核图）。

### 9. 订购信息（Table 6-1，P84）
| 料号 | 封装 | 合封规格 | 供电要求 | 每盘 |
|---|---|---|---|---|
| SF32LB573UB7N6 | QFN68 7×7-T0.9-P0.35 | 32Mb OPI-PSRAM + 128Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB573UB766 | QFN68 7×7-T0.9-P0.35 | 32Mb OPI-PSRAM + 128Mb NOR Flash + 64Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB573UB776 | QFN68 7×7-T1.1-P0.35 | 32Mb OPI-PSRAM + 128Mb NOR Flash + 128Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB575UCNN6 | QFN68 7×7-T0.9-P0.35 | 64Mb OPI-PSRAM | 锂电池供电 | 3000 |
| SF32LB575UC7N6 | QFN68 7×7-T0.9-P0.35 | 64Mb OPI-PSRAM + 128Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB577UDNN6 | QFN68 7×7-T0.9-P0.35 | 128Mb OPI-PSRAM | 锂电池供电 | 3000 |

### 10. 约束禁忌
- **VBUS 不得超过 5.5V**、**VBAT/VCC 不得超过 4.7V**（绝对最大值）；过充保护阈值 4.78V。
- **VDD33_VOUT1/2 各带载不得超过 150mA**。
- **AVDD_BRF 必须接 VSYS**（接 3.3V 会与电池架构不符）。
- VDD_VOUT1/2、VDD_RET、VDD_RTC、VDD18_VOUT 为内部输出，**禁止外部供电**。
- GPADC_VREF / AUD_VREF 接电容到地，**禁止外供电源**。
- **EPAD(69) 必须可靠接地**；BUCK 不可旁路。
- 本系列**无独立 VDDIOA 外部引脚**，GPIO 电平域由内部供给，硬件设计不可按 3.3V 系列方式外接 VDDIOA。

## 关联页面
- 家族总览：[[SF32LB57]]｜3.3V 系列实体：[[SF32LB57X]]
- 来源摘要：[[SF32LB57x_batt_Datasheet_V0.2_20260909]]
- 电源外设（差异权威页）：[[SF32LB57_Peripheral_Power]]
- 其余外设：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Peripheral_Clock]]、[[SF32LB57_Peripheral_GPADC]]、[[SF32LB57_Peripheral_Audio]]、[[SF32LB57_Peripheral_BLE_RF]]、[[SF32LB57_Peripheral_Memory]]

## 原始来源完整引用
1. [DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf]，Raw：`raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf`，Table 4-1~4-3（P40）、Table 4-4~4-6（P41–42）、Table 4-20/4-21（P49）、Table 5-3（P62）、Table 6-1（P84）、最小系统图（P78–82）。

## 待核实问题
1. **电池系列 GPIO 确切数量**未直接给出（3.3V QFN68 为 47 GPIO），待确认。
2. **功耗参数全部 TBD**（Table 4-5/4-6），休眠/待机电流无法核算。
3. **QFN80 / BGA112 封装**：DS5701 已详述其管脚与封装尺寸，但 Table 6-1 订购信息仅列 QFN68 料号（料号缺失为规格书【严重】缺陷，见一致性核查报告），非"后续提供"。
4. 最小系统原理图（P78–82）为矢量图，文本提取反序，关键网络（充电、VBUS 保护、VSYS 去耦）需人工核图。
5. 尚无独立用户手册与硬件设计指南；BOOT/nRST 外部电路、PCB/EMC/ESD 规范缺失。
