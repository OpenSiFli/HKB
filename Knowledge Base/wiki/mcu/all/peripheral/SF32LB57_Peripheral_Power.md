---
title: SF32LB57 电源架构与供电外设
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Power","SF32LB57电源","SF32LB57 电源架构"]
tags: ["企业MCU","外设-电源","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["系列相关-见下表"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 家族**两个系列的差异集中在电源架构与电源专用引脚**。本页为双系列电源对照的权威页：3.3V 系列 [[SF32LB57X]] 由外部 PVDD 供电；电池系列 [[SF32LB57x_batt|SF32LB57x]] 由电池经 VCC 供电并内置充电模块。

> ⚠️ 两份规格书均为 **V0.2 草稿**：`Table 4-5 处理器功耗`、`Table 4-6 BT/BLE 功耗` **全部 TBD**；功耗预算须待量产版确认。

## 1. 双系列电源引脚对照（QFN68 同封装）
| 引脚 | 3.3V 系列 SF32LB57X | 电池系列 SF32LB57x |
|---|---|---|
| 14 | **AVDD33**（模拟电源输入，接 3.3V） | **VDD33_VOUT2**（3.3V LDO2 输出，150mA） |
| 19 | **PVDD**（PMU 电源输入，接 3.3V） | **VSYS**（电源输出 3.0V，外挂电容到地） |
| 20 | **VBATS**（电池电压检测输入） | **VBAT**（电源输出，接电池；内含 ADC 检测） |
| 21 | **VDDIOA**（GPIO 电源输入） | **VBUS**（内部充电模块电源输入） |
| 22 | **NC**（无信号，悬空） | **VDD33_VOUT1**（3.3V LDO1 输出，150mA） |
| 24 | GPIO（非专用脚） | **VCC**（系统电源输入，接电池） |
| 52 | **AVDD_BRF**（接 3.3V） | **AVDD_BRF**（**接 VSYS**） |

**其余电源相关引脚两系列一致（QFN68）**
| 引脚 | 名称 | 类型 | 说明 |
|---|---|---|---|
| 12 | VDD_RTC | PWR | RTC LDO 输出，内部电源，接电容到地 |
| 13 | VDD_RET | PWR | RET LDO 输出，内部电源，接电容到地 |
| 15 | VDD_VOUT2 | PWR | 内部 LDO2 输出，接电容到地 |
| 16 | VDD_VOUT1 | PWR | 内部 LDO1 输出，接电容到地 |
| 17 | BUCK_FB | PWR | Buck 输出，接电感另一端并接电容到地 |
| 18 | BUCK_LX | A,I/O | Buck 电感开关，接电感一端 |
| 23 | VDD18_VOUT | PWR | 1.8V LDO 输出，内部电源，接电容到地 |
| 38 | AVDD33_AUD | PWR | 音频电源输入，接 3.3V 电源 |
| 39 | AUD_VREF | A,I | 音频参考电压输入，接电容到地，**不用外供电源** |
| 68 | GPADC_VREF | A,I | GPADC VREF 输入，接电容到地，**不用外供电源** |
| 69 | EPAD | GND | 地（散热裸焊盘） |

**QFN80（仅 3.3V 系列）额外/差异引脚**
VDDIOA=4、VBATS=5、PVDD=3、NC=2、BUCK_LX=1、BUCK_FB=80、VDD_VOUT1=79、VDD_VOUT2=78、VDD_RET=76、VDD_RTC=75、**VDDIOSB=6（SIP SB IO 电源输入）**、VDD18_VOUT=7、AVDD33=77、GPADC_VREF=63、AVDD_BRF=41、AVDD33_AUD=22、AUD_VREF=23、EPAD=81。

## 2. 3.3V 系列电源架构（SF32LB57X）
- 主电：**PVDD(19) 接外部 3.3V**（范围 2.97~3.63V，绝对最大 3.63V）。
- GPIO 域：**VDDIOA(21)** 独立供电。
- 模拟/射频/音频电源：**AVDD33(14)、AVDD_BRF(52)、AVDD33_AUD(38)** 均接外部 3.3V。
- 内部电源链：PVDD → **Buck**（BUCK_LX 18 / BUCK_FB 17，外接电感+电容，**不可旁路**）→ 内部 LDO 出 VDD_VOUT1(16)/VDD_VOUT2(15)、VDD_RET(13)、VDD_RTC(12)、VDD18_VOUT(23)。
- **提供两路对外 3.3V 供电，每路最大 150mA**（对应电池系列的 VDD33_VOUT1/2；3.3V 系列由片内 LDO 提供，具体输出引脚以引脚表为准）。
- **无充电电路**，不可直接接锂电池。

## 3. 电池系列电源架构（SF32LB57x）
- 电池接 **VCC(24)**（系统电源输入）与 **VBAT(20)**（电源输出/电池电压 ADC 检测）。
- 充电输入 **VBUS(21)**（4.5~5.5V）→ 内部充电模块 → VBAT。
- **VSYS(19)** 为 3.0V 输出，**须外挂电容到地**。
- **AVDD_BRF(52) 接 VSYS**（电池系列射频电源来自 VSYS，而非 3.3V）。
- 对外 3.3V：**VDD33_VOUT1(22)** 与 **VDD33_VOUT2(14)**，各 150mA，接电容到地。
- **无独立 VDDIOA 外部引脚、无 AVDD33 外部输入、无 PVDD**。

## 4. 电气参数（两册 Table 4-1 / 4-2 内容一致）
**运行条件（Table 4-1）**
| Symbol | Description | Min | Typ | Max | Unit |
|---|---|---|---|---|---|
| VBUS | VBUS power input | 4.5 | 5 | 5.5 | V |
| VBAT | VBAT power output | 3.0 | | 4.7 | V |
| VCC | System power input | 3.0* | | 4.7 | V |
| PVDD | System power input | 2.97 | | 3.63 | V |
| Tamb | Ambient temperature | ‑40 | | 85 | °C |
| VIL | CMOS low level input | 0 | | 0.3×VIO | V |
| VIH | CMOS high level input | 0.7×VIO | | VIO | V |
| VTH | CMOS threshold | | 0.5×VIO | | V |
> * 开机电压 3.5V ±10%

**绝对最大值（Table 4-2）**：VBUS 5.5V；VBAT 4.7V；VCC 4.7V；PVDD 3.63V；Tstorage ‑40~125°C

> ⚠️ **说明**：SF32LB57 芯片裸 die 同时支持**电池供电**与**常规 3.3V 供电**两种模式（规格书第 52 页管脚描述等处明确），故两册 Table 4-1/4-2 均含 VBUS/VBAT/VCC 与 PVDD 参数——这是 die 的完整能力描述，**非草稿误植**。QFN68 3.3V 封装（DS5702 Table 5-3）未将 VBUS/VBAT/VCC 引出到封装引脚（pin19/21/22 = PVDD/VDDIOA/NC），因此 3.3V QFN68 版本原理图按引脚表布线、无需连接充电电路；**布线以引脚表（封装管脚定义）为准**。详见来源页一致性核查报告。

## 5. 充电模块（电池系列，Table 4-20）
| 参数 | 符号 | Min | Typ | Max | 单位 |
|---|---|---|---|---|---|
| 充电输入电压 | Vbus | 4.5 | 5 | 5.5 | V |
| BAT 漏电流 | Ileak | | | 30 | nA |
| 恒流充电电流 | Icc | 5 | | 400 | mA |
| 涓流充电电流 | Itri | 0.5 | 30 | 40 | mA |
| 满电截止电流比 | Iend | | 10 | | % of Icc |
| 满电截止电压 | Vcv | 4.2 | | 4.45 | V |
| 满电电压精度 | | | | ±1.5 | % of Vcv |
| 涓流→恒流阈值 | Vcc | | 3 | | V |
| 复充阈值 | Vrechg | | Vcv‑0.15 | | V |
| 过充保护 | Vhigh | | | 4.78 | V |
> ⚠️ **说明**：充电模块为芯片裸 die 共用的内置功能，故该表同时出现在 3.3V 规格书中属正常（非误植）。但 QFN68 3.3V 封装未将 VBUS/VBAT/VCC 引出到封装引脚（pin19/21/22 = PVDD/VDDIOA/NC），故 3.3V 版本原理图无需连接充电电路；电池系列按 DS5701 Table 5-3 连接 VBUS(21)/VBAT(20)/VCC(24)。

## 6. 硬件设计约束
- **3.3V 系列**：PVDD/AVDD33/AVDD33_AUD/AVDD_BRF 均不得超过 **3.63V**。
- **电池系列**：VBUS ≤5.5V，VBAT/VCC ≤4.7V；过充保护 4.78V。
- **BUCK 不可旁路**：BUCK_LX 外接电感、BUCK_FB 外接电容到地。
- **VDD_VOUT1/2、VDD_RET、VDD_RTC、VDD18_VOUT、VDD33_VOUT1/2 均为电源输出**，仅需外接电容，**禁止外部供电**。
- **GPADC_VREF(68)、AUD_VREF(39)** 接电容到地，**不用外供电源**。
- **NC(22，3.3V 系列) 必须悬空**。
- **EPAD(69) 必须可靠接地**。
- **VDD33_VOUT1/2 各带载 ≤150mA**（电池系列）。
- **电池系列 AVDD_BRF 接 VSYS**，不可接 3.3V。

## 关联页面
- 3.3V 实体：[[SF32LB57X]]｜电池实体：[[SF32LB57x_batt|SF32LB57x]]｜家族：[[SF32LB57]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]
- 相关：[[SF32LB57_Peripheral_GPADC]]、[[SF32LB57_Peripheral_Audio]]、[[SF32LB57_Peripheral_Clock]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf`，Table 4-1~4-3（P39）、Table 4-20/4-21（P48）、Table 5-3（P61）、Table 5-4（P62）。
2. [DS5701-SF32LB57x V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf`，Table 4-1~4-3（P40）、Table 4-20/4-21（P49）、Table 5-3（P62）。

## 待核实问题
1. 3.3V 系列是否具备对外 3.3V 输出引脚（特性页称"提供两路对外 3.3V 供电，每路最大 150mA"，但 QFN68 引脚表未标明对应输出脚），待确认。
2. 功耗参数全部 TBD。
3. 两册电气表共用导致的 VBUS/VBAT/VCC 归属问题，待原厂确认。
