---
title: SF32LB52 外设-电源管理
type: mcu_periph
aliases: ["SF32LB52 Power","SF32LB52 多电源域"]
tags: ["企业MCU","外设模块-电源","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_Datasheet_V2.5.5],[SF32LB52x_Datasheet_V0.2.6],[SF32LB52X_UserManual_V0.8.8]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52x(电池)","SF32LB52X(3.3V)"]
series_applicability: ["通用-两系列共用(电源架构按系列区分)"]
hardware_version: ["QFN68L"]
created: 2026-08-10
updated: 2026-08-12
---

## 摘要
SF32LB52 家族（3.3V 系列 SF32LB52X / 电池系列 SF32LB52x）采用片内 PMU（1 路 Buck + 多路 LDO）。**两系列的电源架构与电源专用引脚定义不同，是区分两个系列的核心**：3.3V 系列主电为外部 **PVDD**，电池系列为 **VBUS/VBAT/VCC + 内置 560mA 充电**。本页按系列分别整理电源域、外引脚与电路约束。

> **适用系列**：本页覆盖两系列；请按目标型号所属系列（X=3.3V / x=电池）取用对应小节。家族总览见 [[SF32LB52]]，两系列实体见 [[SF32LB52x_batt|SF32LB52x]] / [[SF32LB52X]]。

## 系列一：3.3V 系列 SF32LB52X（DS5202-SF32LB52X V0.2.6）
### 专用引脚（电源/RF/模拟/IO，DS5202 Table 5-3）
| 引脚 | 名称 | 类型 | 说明 | 电压范围 |
|------|------|------|------|----------|
| 19 | PVDD | PWR | 系统电源输入（型号相关 3.3V/1.8V） | 1.71~3.63V |
| 21 | VDDIOA | PWR | GPIO 电源输入（独立 IO 域） | 随型号 1.8/3.3V |
| 23 | VDD_SIP | PWR | SiP 存储电源 | 随 SiP |
| 14 | AVDD33 | PWR | 模拟电源 | 2.97~3.63V |
| 38 | AVDD33_AUD | PWR | 音频电源 | 2.97~3.63V |
| 52 | AVDD_BRF | PWR | RF 电源 | 2.97~3.63V |
| 13 | VDD_RET | PWR | RET LDO 输出 | — |
| 12 | VDD_RTC | PWR | RTC LDO 输出 | — |
| 17/18 | BUCK_FB / BUCK_LX | PWR / A,I/O | Buck 输出反馈 / 电感开关节点 | — |
| 20 | VBATS | A,I | 电池电压**测量**输入（非主电） | 0~4.7V |
| 68 | GPADC_VREF | A,I | GPADC 参考电压 | — |
| 55/54 | XTAL48M_XI/XO | A,I / A,O | 48MHz 晶振 | — |
| 53 | BRF_ANT | A,I/O | 天线接口 | — |
| 41/40/39/37/36 | ADCP/MIC_BIAS/AUD_VREF/DACP/DACN | — | 音频相关 | — |
| 69 | EPAD | GND | 散热裸焊盘 | 接 GND |

### 电源架构（用户手册 表 3-2）
- 主电 **PVDD**(19)=1.8/3.3V → LDO 出 VDD18_VOUT/VDD_RTC，经 **BUCK** 出 BUCK_FB(1.25V)；BUCK 下游 LDO 出 VDD_VOUT1(HPSYS,1.1V)/VDD_VOUT2(LPSYS,0.9V)/VDD_RET(0.7V)。
- AVDD_BRF(52)/AVDD33(14)/AVDD33_AUD(38) 外部 3.3V；**VDD_SIP**(23) 给合封 Flash/PSRAM（PVDD=1.8V 时 VDD18_LDO 无法出 1.8V，须外部供 VDD_SIP 且关闭 VDD18_LDO）。
- **无充电电路**；VBATS(20) 仅作电池电压测量（0~4.7V），不可直接用作主电源。

## 系列二：电池系列 SF32LB52x（DS5201-SF32LB52x V2.5.5）
### 专用引脚（电源/RF/模拟/IO，DS5201 Table 5-3）
| 引脚 | 名称 | 类型 | 说明 | 电压范围 |
|------|------|------|------|----------|
| 21 | VBUS | PWR | 充电输入 | 4.6~5.5V |
| 20 | VBAT | PWR | 电池电源输出 | 3.2~4.7V |
| 19 | VSYS | PWR | 系统电源输出（内部 LDO，给 AVDD_BRF 等） | — |
| 24 | VCC | PWR | 系统主电源输入 | 3.2~4.7V |
| 23 | VDD18_VOUT | PWR | SiP 存储电源 | — |
| 22 | VDD33_VOUT1 | PWR | 3.3V LDO 输出1（BOOT ROM 自动开启） | 3.3V |
| 14 | VDD33_VOUT2 | PWR | 3.3V LDO 输出2（默认关闭） | 3.3V |
| 16 | VDD_VOUT1 | PWR | 内部 LDO1 输出 | — |
| 15 | VDD_VOUT2 | PWR | 内部 LDO2 输出 | — |
| 13 | VDD_RET | PWR | RET LDO 输出 | — |
| 12 | VDD_RTC | PWR | RTC LDO 输出 | — |
| 17/18 | BUCK_FB / BUCK_LX | PWR / A,I/O | Buck 输出反馈 / 电感开关节点 | — |
| 68 | GPADC_VREF | A,I | GPADC 参考电压 | — |
| 55/54 | XTAL48M_XI/XO | A,I / A,O | 48MHz 晶振 | — |
| 53 | BRF_ANT | A,I/O | 天线接口 | — |
| 52 | AVDD_BRF | PWR | RF 电源（可接 VSYS） | 2.97~3.63V |
| 41/40/39/38/37/36 | ADCP/MIC_BIAS/AUD_VREF/AVDD33_AUD/DACP/DACN | — | 音频相关 | — |
| 69 | EPAD | GND | 散热裸焊盘 | 接 GND |

> **GPIO IO 域供电（已确认）**：电池系列**外部无独立 VDDIOA 引脚**（引脚 21 为 VBUS 充电输入）；片内 VDDIOA 在芯片内部直接连到 **VSYS** 引脚，GPIO IO 电平跟随 VSYS。即电池系列 GPIO 由 VSYS 经内部 VDDIOA 供电，无需外部 VDDIOA 管脚。
> **两系列引脚定义差异范围（已确认）**：SF32LB52X（3.3V）与 SF32LB52x（电池）**仅引脚 19~24 与引脚 14 的引脚定义不同**，其余引脚（PA00–PA44 GPIO 复用矩阵）**基本一致，唯一例外是 PA21**：PA21 仅存在于 3.3V 系列（pin24=PA21）；电池系列 pin24 为电源引脚 VCC、**无 PA21**。因此 **3.3V 系列共 45 GPIO、电池系列共 44 GPIO**。差异集中于电源/充电专用引脚（19 PVDD↔VSYS、20 VBATS↔VBAT、21 VDDIOA↔VBUS、22/24 对应电源输出、23 VDD_SIP↔VDD18_VOUT、14 AVDD33↔VDD33_VOUT2）。

### 电源架构（用户手册 表 3-1）
- **VBUS**(21,5V 充电输入)/**VBAT**(20,4V 充电输出)/**VCC**(24,4V 主电) → 内部 LDO 出 VSYS(3.3V, 给 AVDD_BRF)；VDD33_VOUT1(3.3V, BOOT ROM 自动开启, 给 AVDD33_AUD/外 Flash)、VDD33_VOUT2(3.3V, 默认关闭)；**内置 560mA 锂电充电，满电 4.2~4.45V**。
- 其余内部轨（BUCK_FB 1.25V、VDD_VOUT1/2、VDD_RET、VDD_RTC）同 3.3V 系列。

### 充电器全参数（DS5201 Table 4-18，P38）
| 参数 | 符号 | Min | Typ | Max | 单位 |
|------|------|-----|-----|-----|------|
| 充电器输入电压 | Vbus | 4.6 | 5 | 5.5 | V |
| BAT 漏电流 | Ileak | — | 30 | — | nA |
| 恒流充电电流 | Icc | 5 | — | 560 | mA |
| 涓流充电电流 | Itri | 0.5 | 56 | 56 | mA |
| 充满终止电流比 | Iend | 10% | — | — | of Icc |
| 充满终止电压 | Vcv | 4.2 | — | 4.45 | V |
| 满电电压精度 | — | ±1.5% | — | — | of Vcv |
| 涓流→恒流切换阈值 | Vcc | 3 | — | — | V |
| 再充电阈值 | Vrechg | Vcv‑0.15 | — | — | V |
| 过充保护电压 | Vhigh | 4.5 | — | — | V |

### 电池输入 VBAT 范围（DS5201「Others」，P6）
- V2.5.5 明确 **VBAT 电池电源输入范围 3.2–4.7V**；与 3.3V 系列的 `VBATS(20)` 电池电压**测量**输入 0~4.7V 为不同引脚/含义。

## 两系列通用电路要求与约束禁忌
- 各电源域须分别满足推荐工作条件（Table 4-1）并加合适去耦电容（具体容值/布局见参考设计，datasheet 文本未逐域给出，待核实）。
- **PVDD 取值随型号（仅 3.3V 系列）**：DS5202 Table 5-7 中部分型号 3.3V、部分 1.8V；原理图取电务必核对订购型号。
- Buck 外围：BUCK_LX 接功率电感至 BUCK_FB（反馈），按参考设计取值；USB/模拟/RF 等独立 LDO 输入需单独滤波。
- 任一电源缺失或超绝对最大值（+3.63V / ‑0.3V）将导致功能异常或永久损伤。
- EPAD（69）须可靠接 GND，否则散热/回流焊可靠性不达标。
- 多电源域上电/掉电时序建议遵循 PMU 架构（Fig 1-3），避免闩锁。
- **BUCK（FB/LX）不可旁路、不可被外部 LDO 替代**；启动后自动开启、hibernate 后自动关闭。
- VDD33_VOUT1 由 BOOT ROM 自动开启；VDD33_VOUT2 默认关闭需软件开启。
- MIC_BIAS 默认关闭，需 AUDCODEC 寄存器开启并调压。
- 合封存储外部供电须由 **PA21** 控制以防 hibernate 漏电（见 [[DR_LowPower_IO_Retention]]、[[CR_Hibernate_SiP_Supply]]）。

> 各电源域去耦电容、Buck 电感/反馈电阻具体值手册未列，仍属待核实（需补参考设计）。

## 关联页面
- 电池系列实体：[[SF32LB52x_batt|SF32LB52x]]｜3.3V 系列实体：[[SF32LB52X]]｜家族总览：[[SF32LB52]]
- GPIO：[[SF32LB52_Peripheral_GPIO]]｜时钟：[[SF32LB52_Peripheral_Clock]]｜BLE_RF：[[SF32LB52_Peripheral_BLE_RF]]
- 校验规则：[[CR_PowerDomains]]、[[CR_AbsMaxRatings]]、[[CR_EPAD_GND]]、[[CR_VBATS_Range]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§1.4（P8–P9）、Table 4-1/4-2（P29）、Table 5-3（P47）、Table 5-7（P50）
2. [DS5201-SF32LB52x-Datasheet V2p5p5.pdf]，Raw：raw/mcu/all_chip/datasheets/DS5201-SF32LB52x-Datasheet V2p5p5.pdf，Table 5-3（P48）、§1.4/§4.5（P38）、「Others」（P6）、Table 4-18（P38）、Table 5-7（P51）
3. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§3 电源架构（P39–P46）

## 待核实问题
- 各电源域推荐去耦电容容值/数量、Buck 电感与反馈电阻具体值，datasheet 文本未给出，待补 SiFli 参考原理图（raw/mcu/ref_design/）。
- （已确认）电池系列 GPIO IO 域由内部 VDDIOA→VSYS 供电，外部无 VDDIOA 引脚，无需再核对 UM5201，详见上方「GPIO IO 域供电」说明。
- 3.3V 系列与电池系列**仅引脚 19~24 与 14 的引脚定义不同，其余完全一致（已确认）**；电源/充电专用引脚映射以对应 datasheet Table 5-3 为准。
