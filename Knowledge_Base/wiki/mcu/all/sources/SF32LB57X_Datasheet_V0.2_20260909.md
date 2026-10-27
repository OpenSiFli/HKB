---
title: DS5702-SF32LB57X 芯片技术规格书 V0.2（2026-09-09）
type: mcu_source
aliases: ["SF32LB57X_Datasheet_V0.2","DS5702-SF32LB57X-CN","SF32LB57X规格书"]
tags: ["企业MCU","来源文档","规格书/datasheet","芯片系列-SF32LB57","3.3V供电系列"]
doc_type: datasheet
doc_version: V0.2
doc_date: 2026-09-09
doc_status: 草稿（0.0.0~0.9.9，非正式发布，参数随时可能更改）
vendor: 思澈科技（南京）有限公司 SiFli
sources: ["[[raw/mcu/all_chip/datasheets/DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf]]"]
mcu_family: ["SF32LB57"]
mcu_series: ["3.3V供电系列"]
mcu_model: ["SF32LB57X"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SiFli **SF32LB57X（大写 X）= 3.3V 供电系列** 芯片技术规格书。文档编号 **DS5702-SF32LB57X-CN**，版本 V0.2（2026-08-29 更新），PDF 共 84 页。

> 📌 **系列判定**：文档标题大小写与芯片命名**一致**——`DS5702-SF32LB57X`（大写 X）= 3.3V 系列；电池系列为 `DS5701-SF32LB57x`（小写 x）。与 SF32LB52 家族规则相同。

## 文档状态（重要）
- 本版为 **草稿（V0.2）**，按文档第 2 页「文档状态说明」：0.0.0~0.9.9 为初稿，**信息为初步数据，反映量产前产品的规格与性能，不能保证准确性，随时可能更改，思澈科技不会主动通知**。
- 实测影响：**Table 4-5 处理器功耗、Table 4-6 BT/BLE 功耗全部为 TBD**；引用功耗参数前须向原厂确认量产版本。

## 芯片核心规格（本册）
- 内核：双 Arm Cortex-M33 STAR-MC1 @240MHz（HPSYS 双性能核），1968 CoreMark
  - HCPU：32KB(2-way) I$ + 16KB(4-way) D$；ACPU：16KB(2-way) I$ + 8KB(4-way) D$
  - HPSYS SRAM 512KB（全部 Retention）；LPSYS Cortex-M33 @24MHz + SRAM 80KB（全部 Retention）；合计 **592KB**
- 图形：2D/2.5D **ePicasso 3.0** 引擎，最大 2048×2048；**eZip 3.0** 解压加速器（eZip/eZip-A 无损、JPEG/MJPEG 有损）
- 显示：LCD 控制器支持 8080 / SPI·Dual·Quad-SPI / DPI(RGB) / JDI / 8-16b EPD；DCMI 摄像头（DVP / SPI 系列）
- 无线：双模蓝牙 **6.3**（支持 BLE Audio、LE LR）；BLE 灵敏度 ‑100dBm(1Mbps) / ‑107.5dBm(S8)；最大发射 17dBm(BR/BLE) / 13dBm(EDR2/3)
- 音频：1×24-bit DAC（SNR 109dB、Noise floor 3.7µVrms）、2×24-bit ADC（SNR 97dB）、Micbias LDO 1.4~2.8V/0~2mA
- 存储：SiP NOR-Flash ≤104MHz、SiP OPI-PSRAM ≤156MHz；3×MPI(QSPI)（NOR/NAND/QPI-PSRAM）、2×SD/SDIO（SD3.0/SDIO3.0/eMMC）
- 外设：58 GPIO + 6 GPO MPI IO；3×UART、4×I2C、2×SPI、2×I2S、2×PDM、1×USB2.0 FS、**2×CAN**、GPDMA、PTM
- 模拟：1×12-bit SAR ADC（12 通道，4Msps）、1×片上温度传感器
- 定时器：2×16b GPTIM、4×32b BTIM、2×32b ATIM、2×24b LPTIM、1×PWM、1×RTC、2×24b WDT、1×IWDT
- 安全：AES/HASH/CRC、TRNG、eShield、PSA Certified Level 1
- 电源管理：内置高效率 Buck + 低功耗 LDO；**提供两路对外 3.3V 供电，每路最大 150mA**；休眠功耗 1µA@3.3V（特性页宣称，Table 4-6 全 TBD 待核实）
- 工作温度：‑40 ~ +85 °C
- 封装与 GPIO：QFN68 7×7（3.3V 供电，47 GPIO）／QFN80 8×8（3.3V 供电，58 GPIO）／BGA112 5.4×4.4（3.3V 供电，最多 58 GPIO + 6 GPO MPI IO）

## 关键章节页码索引（PDF 页）
| 内容 | PDF 页 | 备注 |
|---|---|---|
| 更新历史 / 文档状态 | 2 | 草稿声明 |
| 产品概述 / 功能框图 | 3 | |
| 产品特性 | 4–5 | CPU/图形/无线/音频/外设/封装 |
| 目录 / 插图 / 表格 | 7–10 | |
| 常用接口速率（Table 3-1） | 38 | MPI 156/104MHz、SDMMC 48MHz、I2C 3.4MHz、SPI 48MHz、UART 3Mbaud、GPADC 4Msps |
| CAN 特性 | 38 | CAN2.0b，不支持 CAN FD，最高 1Mbps |
| 运行条件 Table 4-1 | 39 | 含 VBUS/VBAT/VCC 项（die 双供电模式完整能力，非误植；3.3V QFN68 未引出，见一致性核查报告） |
| 绝对最大值 Table 4-2 | 39 | PVDD 3.63V、Tstorage ‑40~125°C |
| I/O 特性 @3.3V Table 4-3 | 39 | IOH/IOL 12/30/38mA、RPU/RPD 7/10/20kΩ |
| 可靠性测试 Table 4-4 | 40 | HBM ±4000V、CDM ±1000V、MSL3 |
| 处理器功耗 Table 4-5 | 40 | ⚠️ **全部 TBD** |
| BT/BLE 功耗 Table 4-6 | 41 | ⚠️ **全部 TBD** |
| BLE 射频 TX/RX Table 4-7~4-12 | 41–44 | 1M/2M/S2/S8 |
| 经典蓝牙 TX/RX Table 4-13~4-17 | 45–47 | BR/EDR |
| 音频 ADC Table 4-18 | 47 | 24bit、SNR 97dB |
| 音频 DAC Table 4-19 | 48 | 24bit、SNR/DR 109dB |
| 充电模块电气 Table 4-20 | 48 | die 共用内置功能；3.3V QFN68 未引出 VBUS/VBAT，故 3.3V 版不接充电 |
| IO 驱动能力 Table 4-21 | 48 | DS1/DS0 → 2/4/8/12mA |
| GPADC 特性 Table 4-22 | 49 | 12-bit |
| 管脚布局 / 管脚描述 | 50–51 | |
| GPIO(PA) 列表 Table 5-2 | 52、54 | |
| 专用管脚 Table 5-3（QFN68） | 61 | 3.3V 系列权威引脚表 |
| 专用管脚 Table 5-4（QFN80） | 62 | |
| 封装尺寸 / 回流焊 | 64–76 | QFN80 尺寸、MSL、回流曲线 |
| 硬件最小系统原理图 | 77 | 含 Boot 分支/存储类型判别说明（图为矢量，文本反序） |
| 订购信息 Table 6-1 | 83 | 5 个料号 |

## 关联页面
- 芯片实体（3.3V 系列）：[[SF32LB57X]]｜家族总览：[[SF32LB57]]｜电池系列规格书：[[SF32LB57x_Datasheet_V0.2_20260909]]
- 外设：[[SF32LB57_Peripheral_Power]]、[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Peripheral_Clock]]、[[SF32LB57_Peripheral_GPADC]]、[[SF32LB57_Peripheral_Audio]]、[[SF32LB57_Peripheral_BLE_RF]]、[[SF32LB57_Peripheral_Serial]]、[[SF32LB57_Peripheral_Memory]]、[[SF32LB57_Peripheral_Timer_PWM]]、[[SF32LB57_Peripheral_Display]]、[[SF32LB57_Peripheral_USB]]
- 同家族方法学参考：[[SF32LB52X_Datasheet_V0.2.6]]（52 家族处理范式）
- 内部一致性核查报告：`raw/mcu/all_chip/datasheets/一致性核查报告_DS5702_V0p2-20260909.md`（DS5702 本册前后自洽核查）

## 原始来源完整引用
1. [DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf]，Raw：`raw/mcu/all_chip/datasheets/DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf`，84 页；原件另存于 `D:/.workbuddy/DS/`（仅复制未移动）。

## 待核实问题
1. **Table 4-1 运行条件同时列出 VBUS/VBAT/VCC 与 PVDD**：此为芯片裸 die 同时支持电池与 3.3V 两种供电模式的完整能力描述（规格书第 52 页管脚描述明确"常规 3.3V 供电时接 3.3V 电源"），**非草稿误植**。QFN68 3.3V 封装（Table 5-3）未将 VBUS/VBAT/VCC 引出到封装引脚（pin19/21/22 = PVDD/VDDIOA/NC），故 3.3V QFN68 版本按引脚表布线、不接充电电路；VBUS/VBAT/VCC 参数属 die 全能力，原理图布线以引脚表为准。
2. **Table 4-20 充电模块电气特性出现在 3.3V 规格书中**属正常（die 共用内置功能），非误植；3.3V QFN68 封装未引出 VBUS/VBAT，无需连接充电。
3. **功耗参数全部 TBD**（Table 4-5/4-6），无法用于低功耗预算核算，须等量产版。
4. 订购信息中 `SF32BPRTUN3N6` 料号命名与同表其余 `SF32LB57xxxxx` 不一致，疑为文档笔误，待原厂确认。
5. QFN80 表 Table 5-4 中 AVDD_BRF 描述残留「电池供电时和 VSYS 接一起」字样，为共用模板痕迹；3.3V 常规供电时应接 3.3V 电源。
6. 尚无独立用户手册（UM）与硬件设计指南；BOOT/nRST 外部电路、PCB 布局、EMC/ESD 设计规范待补。
