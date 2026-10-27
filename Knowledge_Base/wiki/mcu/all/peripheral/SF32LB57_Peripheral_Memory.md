---
title: SF32LB57 存储接口（MPI / SD-SDIO-eMMC / SiP）
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Memory","SF32LB57存储","SF32LB57 MPI","SF32LB57 SDMMC"]
tags: ["企业MCU","外设-存储接口","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 存储资源：**3× MPI（QSPI）**、**2× SD/SDIO/eMMC**，支持 SiP 合封 NOR-Flash 与 OPI-PSRAM，以及外挂 QSPI-NOR/NAND、SD-NAND、eMMC。**两系列一致**。

## 1. 存储架构
**片上 / 合封（SiP）**
- 片上 SRAM **592KB**（HPSYS 512KB + LPSYS 80KB，全部 Retention）
- SiP 合封（随料号）：**OPI-PSRAM**（≤156MHz，DDR）、**QSPI-NOR Flash**（≤104MHz，DTR）

**外部扩展**
- **3× MPI（QSPI）**：支持 **NOR、NAND、QPI-PSRAM**；外挂 QSPI-NOR / QSPI-NAND Flash（SDR）≤**104 MHz**
- **2× SD/SDIO**：支持 **SD3.0、SDIO3.0、eMMC**；SDMMC ≤**48 MHz**
- 支持 Flash 实时（on-the-fly）解密（eShield 安全架构）

## 2. 速率汇总（Table 3-1）
| 控制器 | 最高速率 | 备注 |
|---|---|---|
| MPI1 | 156 MHz（OPI-PSRAM，DDR）/ 104 MHz（QSPI-NOR，DTR） | 合封 |
| MPI2 | 156 MHz（OPI-PSRAM，DDR）/ 104 MHz（QSPI-NOR，DTR） | 合封 |
| MPI3 | 104 MHz | 外挂 QSPI-NOR / QSPI-NAND Flash（SDR） |
| SDMMC | 48 MHz | 外挂 eMMC |

## 3. 启动存储类型判别（最小系统图，DS5702 P77）
3.3V 系列最小系统原理图给出 **Boot 分支 / 主机侧 Boot 开关 / Boot 寄存器** 结构，通过配置电平（L/H）选择启动存储介质：
| 启动存储 | 配置电平 |
|---|---|
| SPI NOR Flash | L / L |
| SPI NAND Flash | H / L |
| SD NAND Flash | L / H |
| eMMC | H / H |
> ⚠️ 该图为矢量图，**文本提取为反序**，上表由反序文本解译得到，**须人工核图确认**。相关信号名疑似 `MEM_CFG0` / `MEM_CFG1`（反序文本 `0GFC_MEM` / `1GFC_MEM`）。
>
> 📌 与 SF32LB52 家族对照：52 家族用于**判别存储类型**的是 **PA13 / PA17**（SD_D3 / SD_D1），且**与 BMR[0] 无关**（BMR[0] 为 ROM 启动流程标志位）。57 家族对应机制待补用户手册确认。

## 4. 硬件设计约束
- 外挂 Flash / PSRAM 走线尽量短，QSPI 时钟与数据线等长、包地处理。
- **外挂存储供电控制**：待机/关机场景需评估存储漏电；SPI Nand / SD Nand 通常须控制供电（SF32LB52 家族经验：Nor Flash 可进 Deep Power Down 常供电，Nand/SD Nand 须控供电）。⚠️ 57 家族具体控制引脚待补参考设计。
- SD/SDIO 的 CMD / D3 等信号在初始化阶段须有确定电平，**通常需要外部上拉**（具体阻值待补 57 家族参考设计）。
- MPI 与 SDMMC 若复用同一组 IO，须确认不可同时启用（SF32LB52 家族存在 MPI2/SDMMC 互斥，57 家族待确认）。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- GPIO/复用：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Pinmux]]
- 时钟：[[SF32LB57_Peripheral_Clock]]｜来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Table 3-1（P38）、§3.8 存储接口（P26–27）、图 3-10 MPI 控制器框图（P26）、图 3-11 寄存器模式时序（P27）、最小系统图（P77，Boot 分支/存储类型）。
2. [DS5701-SF32LB57x V0.2]，同上（P38–39 / P27 / P78–82）。

## 待核实问题
1. **启动存储类型判别信号**（MEM_CFG0/1 或对应 GPIO）的权威说明待用户手册补入；最小系统图为矢量图，文本反序。
2. **SD/SDIO/eMMC 上拉电阻**推荐值本册未给出，禁止套用 SF32LB52 的 7.5kΩ。
3. MPI 与 SDMMC 是否存在 IO 复用互斥，待确认。
4. 各 MPI / SDMMC 实例对应 GPIO 复用引脚，待补 Pinmux。
5. 外挂存储在低功耗（hibernate/standby）下的供电控制策略与对应 GPIO，待补参考设计。
