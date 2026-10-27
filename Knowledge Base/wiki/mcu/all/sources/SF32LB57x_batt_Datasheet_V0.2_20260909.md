---
title: DS5701-SF32LB57x 芯片技术规格书 V0.2（2026-09-09）
type: mcu_source
aliases: ["SF32LB57x_Datasheet_V0.2","DS5701-SF32LB57x-CN","SF32LB57x规格书"]
tags: ["企业MCU","来源文档","规格书/datasheet","芯片系列-SF32LB57","电池供电系列"]
doc_type: datasheet
doc_version: V0.2
doc_date: 2026-09-09
doc_status: 草稿（0.0.0~0.9.9，非正式发布，参数随时可能更改）
vendor: 思澈科技（南京）有限公司 SiFli
sources: ["[[raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf]]"]
mcu_family: ["SF32LB57"]
mcu_series: ["电池供电系列"]
mcu_model: ["SF32LB57x"]
hardware_version: ["QFN68 7x7","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SiFli **SF32LB57x（小写 x）= 电池供电系列** 芯片技术规格书。文档编号 **DS5701-SF32LB57x-CN**，版本 V0.2（2026-08-29 更新），PDF 共 85 页。

> 📌 **系列判定**：文档标题大小写与芯片命名**一致**——`DS5701-SF32LB57x`（小写 x）= 电池系列；3.3V 系列为 `DS5702-SF32LB57X`（大写 X）。与 SF32LB52 家族规则相同。
>
> 📌 **NTFS 命名说明**：本页文件名带 `_batt` 后缀，因 Windows/NTFS 不区分大小写，`SF32LB57X_*.md` 与 `SF32LB57x_*.md` 会被视为同一文件。引用本页请用 `[[SF32LB57x_batt_Datasheet_V0.2_20260909|SF32LB57x 规格书]]`。

## 文档状态（重要）
- 本版为 **草稿（V0.2）**：0.0.0~0.9.9 为初稿，信息为初步数据，反映量产前规格，**不能保证准确性，随时可能更改，不主动通知**。
- 实测影响：**Table 4-5 处理器功耗、Table 4-6 BT/BLE 功耗全部为 TBD**。

## 电池系列专属要点（本册权威）
依据 **Table 5-3（QFN68，57xUxxx6）专用管脚表**，电池系列电源引脚如下：

| 引脚 | 名称 | 类型 | 说明 |
|---|---|---|---|
| 21 | VBUS | PWR | **内部充电模块的电源输入口** |
| 20 | VBAT | PWR | 电源输出，接电池；内部有 ADC 检测电池电压值 |
| 19 | VSYS | PWR | 电源输出 3.0V，外挂电容到地 |
| 24 | VCC | PWR | 系统电源输入，接电池 |
| 22 | VDD33_VOUT1 | PWR | 3.3V LDO1 输出，接电容到地，带载能力 **150mA** |
| 14 | VDD33_VOUT2 | PWR | 3.3V LDO2 输出，接电容到地，带载能力 **150mA** |
| 23 | VDD18_VOUT | PWR | 1.8V LDO 输出，内部电源，接电容到地 |
| 52 | AVDD_BRF | PWR | 射频电源输入，**接 VSYS** |
| 38 | AVDD33_AUD | PWR | 音频电源输入，接 3.3V 电源 |
| 18/17 | BUCK_LX / BUCK_FB | A,I/O / PWR | Buck 电感开关 / Buck 输出（接电感另一端并接电容到地） |
| 16/15 | VDD_VOUT1 / VDD_VOUT2 | PWR | 内部 LDO1/LDO2 输出，接电容到地 |
| 13/12 | VDD_RET / VDD_RTC | PWR | RET/RTC LDO 输出，接电容到地 |
| 68 | GPADC_VREF | A,I | GPADC VREF 输入，接电容到地，**不用外供电源** |
| 55/54 | XTAL48M_XI / XO | A,I / A,O | 48MHz 晶体接口 |
| 53 | BRF_ANT | A,I/O | 天线接口 |
| 39 | AUD_VREF | A,I | 音频参考电压输入，接电容到地，不用外供电源 |
| 37/36 | DACP / DACN | A,O | 音频 DAC 输出 |
| 69 | EPAD | GND | 地 |

**与 3.3V 系列（[[SF32LB57X]]）的引脚差异（同 QFN68 封装对照）**
| 引脚 | 3.3V 系列 SF32LB57X | 电池系列 SF32LB57x |
|---|---|---|
| 14 | AVDD33（模拟电源输入，接 3.3V） | VDD33_VOUT2（3.3V LDO2 输出，150mA） |
| 19 | PVDD（PMU 电源输入，接 3.3V） | VSYS（电源输出 3.0V） |
| 20 | VBATS（电池电压检测输入） | VBAT（电源输出，接电池） |
| 21 | VDDIOA（GPIO 电源输入） | VBUS（充电模块电源输入） |
| 22 | NC（无信号） | VDD33_VOUT1（3.3V LDO1 输出，150mA） |
| 24 | GPIO（非专用脚） | VCC（系统电源输入，接电池） |
| 52 | AVDD_BRF（接 3.3V） | AVDD_BRF（**接 VSYS**） |

> 结论：两系列**仅电源专用引脚不同**（pin 14/19/20/21/22/24 与 AVDD_BRF 供电源），其余外设/射频/音频/晶体/GPADC/地引脚一致；电池系列因 pin24 被 VCC 占用，**GPIO 数量比 3.3V 系列少 1 个**（待原厂确认具体数）。

## 共享规格（与 3.3V 系列一致，详见 [[SF32LB57X_Datasheet_V0.2_20260909]]）
双核 Cortex-M33 STAR-MC1 @240MHz/24MHz、1968 CoreMark、592KB SRAM、2D/2.5D ePicasso 3.0、eZip 3.0、BT/BLE 6.3、24-bit 音频 ADC/DAC、3×MPI + 2×SD/SDIO、58 GPIO+6 GPO MPI IO、3×UART/4×I2C/2×SPI/2×I2S/2×PDM/USB2.0 FS/2×CAN、12-bit GPADC×12 通道、‑40~+85°C。

## 关键章节页码索引（PDF 页；电池册比 3.3V 册多 1 页）
| 内容 | PDF 页 | 备注 |
|---|---|---|
| 更新历史 / 文档状态 | 2 | 草稿声明 |
| 产品概述 / 功能框图 | 3 | |
| 产品特性 | 4–5 | |
| 电源管理架构（图 1-3） | 19 | 含 VSYS/VBAT/VBUS/VCC 关系 |
| 运行条件 Table 4-1 | 40 | VBUS 4.5~5.5V、VBAT 3.0~4.7V、VCC 3.0~4.7V、PVDD 2.97~3.63V |
| 绝对最大值 Table 4-2 | 40 | VBUS/VBAT/VCC 4.7V、PVDD 3.63V |
| I/O 特性 @3.3V Table 4-3 | 40 | IOH/IOL 12/30/38mA |
| 可靠性测试 Table 4-4 | 41 | HBM ±4000V、CDM ±1000V、MSL3 |
| 处理器功耗 Table 4-5 | 41 | ⚠️ 全部 TBD |
| BT/BLE 功耗 Table 4-6 | 42 | ⚠️ 全部 TBD |
| BLE / 经典蓝牙射频 | 42–48 | |
| 音频 ADC/DAC Table 4-18/4-19 | 48–49 | |
| 充电模块电气 Table 4-20 | 49 | **本系列适用** |
| IO 驱动能力 Table 4-21 | 49 | DS1/DS0 → 2/4/8/12mA |
| GPIO(PA) 列表 Table 5-2 | 53、55 | |
| 专用管脚 Table 5-3（QFN68） | 62 | **电池系列权威引脚表** |
| 专用管脚（次封装） | 63–65 | |
| 封装尺寸 / 回流焊 | 65–76 | |
| 硬件最小系统原理图 | 78–82 | |
| 订购信息 Table 6-1 | 84 | 6 个料号，全部 QFN68 锂电池供电 |

## 订购信息（Table 6-1，P84）
| 料号 | 封装 | 合封规格 | 供电要求 | 每盘 |
|---|---|---|---|---|
| SF32LB573UB7N6 | QFN68 7×7-T0.9-P0.35 | 32Mb OPI-PSRAM + 128Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB573UB766 | QFN68 7×7-T0.9-P0.35 | 32Mb OPI-PSRAM + 128Mb NOR Flash + 64Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB573UB776 | QFN68 7×7-T1.1-P0.35 | 32Mb OPI-PSRAM + 128Mb NOR Flash + 128Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB575UCNN6 | QFN68 7×7-T0.9-P0.35 | 64Mb OPI-PSRAM | 锂电池供电 | 3000 |
| SF32LB575UC7N6 | QFN68 7×7-T0.9-P0.35 | 64Mb OPI-PSRAM + 128Mb NOR Flash | 锂电池供电 | 3000 |
| SF32LB577UDNN6 | QFN68 7×7-T0.9-P0.35 | 128Mb OPI-PSRAM | 锂电池供电 | 3000 |
> 注：电池系列**订购信息（Table 6-1）仅列 QFN68 料号**；DS5701 已详述 QFN80/BGA112 管脚与封装尺寸，但 V0.2 中其料号缺失（规格书【严重】缺陷，见一致性核查报告），非硬件不支持。3.3V 系列另有 QFN80 / BGA112。

## 关联页面
- 芯片实体（电池系列）：[[SF32LB57x_batt]]｜家族总览：[[SF32LB57]]｜3.3V 系列规格书：[[SF32LB57X_Datasheet_V0.2_20260909]]
- 电源外设（双系列差异）：[[SF32LB57_Peripheral_Power]]
- 其余外设：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Peripheral_Clock]]、[[SF32LB57_Peripheral_GPADC]]、[[SF32LB57_Peripheral_Audio]]、[[SF32LB57_Peripheral_BLE_RF]]、[[SF32LB57_Peripheral_Memory]]
- 内部一致性核查报告：`raw/mcu/all_chip/datasheets/一致性核查报告_V0p2-20260909.md`（DS5701 本册前后自洽核查，含订购信息缺失 QFN80/BGA112 料号【严重】项）

## 原始来源完整引用
1. [DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf]，Raw：`raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf`，85 页；原件另存于 `D:/.workbuddy/DS/`（仅复制未移动）。

## 待核实问题
1. **充电模块参数（Table 4-20）** 在两册中完全相同：Vbus 4.5~5.5V、BAT 漏电流 30nA、恒流充电 5~400mA、涓流 0.5~30~40mA、截止电流比 10% Icc、截止电压 Vcv 4.2~4.45V、满电精度 ±1.5%、涓流转恒流阈值 3V、复充阈值 Vcv‑0.15V、过充保护 4.78V。充电模块为 die 共用内置功能，故两册均含此表属正常；3.3V QFN68 封装未引出 VBUS/VBAT，按引脚表判定 3.3V 系列不接充电。
2. **电池系列 GPIO 确切数量**未直接给出（3.3V QFN68 为 47 GPIO），待确认。
3. **功耗全部 TBD**，休眠/待机电流无法核算（特性页宣称休眠 2.8µA@3.8V，与表 4-6 TBD 待核实）。
4. **QFN80 / BGA112 封装**：DS5701 已详述其管脚与封装尺寸，但 Table 6-1 订购信息仅列 QFN68 料号（料号缺失为规格书【严重】缺陷，见一致性核查报告），非"后续提供"。
5. 尚无独立用户手册与硬件设计指南；电池供电最小系统原理图（P78–82）为矢量图，文本提取为反序，关键网络需人工核图确认。
