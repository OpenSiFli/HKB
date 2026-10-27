---
title: CR-Checklist-存储
type: mcu_check_rule
aliases: ["CR_Checklist_Storage","存储审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重","来源-官方Checklist"]
sources: [[SF32LB52_Checklist_V0.1_20241008]]
mcu_family: ["SF32LB52"]
series_applicability: ['通用-两系列共用']
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SiFli 官方 **SF32LB52 硬件设计 Checklist（V0.1 20241008）**〈存储〉章节，提炼为原理图 AI 审图规则。共 11 条核查事项，逐条保留官方「适用芯片」映射（已归一化为 通用-两系列共用），供设计评审与 PDF 原理图 AI 审图逐项核对。

## 核心硬件内容（背景）
本规则为官方黄金样板 Checklist 的同源转化，非本文独创。每条「核查要点」即官方对硬件设计的硬性/推荐要求；参数（电压范围、电容容值/耐压、线宽、上拉阻值、ESR/ppm、阻抗等）以官方 Checklist 原文为准。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析或设计评审时，逐项核对下方〈存储〉清单的每条「核查要点」。
2. **违规现象描述**：任一条「核查要点」未满足即视为违规（如电压越界、电容/线宽不达标、上拉缺失、IO 电平不匹配、布局/屏蔽违规、ESD 缺失等）。
3. **风险影响说明**：依条目性质而异——电源/存储/ESD 类违规可致器件永久损坏或功能失效（严重/致命）；时钟/射频/显示/音频类违规致性能劣化或 EMC 不通过（一般/优化）。
4. **标准化整改方案**：按各条目「核查要点」整改至满足官方参数（含选型、容值、线宽、布局、防护器件）。
5. **知识库溯源依据**：[[SF32LB52_Checklist_V0.1_20241008]]（〈存储〉章节）。

| 序号 | 核查事项 | 适用芯片(系列) | 核查要点 |
| -- |--|--|--|
| 1 | MPI3 外接 SPI NOR Flash 引脚上拉检查 | 通用-两系列共用 | PA13(MPI D1)、PA17(MPI D3) 无需上拉电阻 |
| 2 | MPI3 外接 SPI NAND Flash 引脚上拉检查 | 通用-两系列共用 | PA13(MPI D1) 无需上拉；PA17(MPI D3) 必须接7.5kΩ上拉电阻 |
| 3 | MPI3 外接 SD NAND Flash 引脚上拉检查 | 通用-两系列共用 | PA13(SD D3)、PA15(SD CMD) 必须接7.5kΩ上拉电阻；PA17(SD D1) 无需上拉 |
| 4 | MPI3 外接 eMMC 引脚上拉检查 | 通用-两系列共用 | PA13(SD D3)、PA17(SD D1)、PA15(SD CMD) 全部必须接7.5kΩ上拉电阻 |
| 5 | MPI3 外接存储电源控制电路核查 | 通用-两系列共用 | 1. SPI NOR Flash：可常供电；；2. SPI NAND / SD NAND / eMMC：必须增加电源开关控制；；3. 外部介质启动场景：存储电源默认上电导通 |
| 6 | 外接存储颗粒型号合规性核查 | 通用-两系列共用 | 选用的存储颗粒型号需在项目AVL认证清单内 |
| 7 | 存储颗粒IO电平匹配核查 | 通用-两系列共用 | 存储颗粒工作电压范围与主芯片IO供电电平保持一致 |
| 8 | 外挂存储器类型检查 | 通用-两系列共用 | 内部合封了Flash的型号，外部只能接SPI Nor Flash |
| 9 | 外挂存储器电源控制信号GPIO检查 | 通用-两系列共用 | 电池供电系列用PA11，3.3V供电系列用PA21 |
| 10 | EMC检查 | 通用-两系列共用 | 时钟线靠近源端串33欧电阻，电阻后预留并联电容位 |
| 11 | 外挂双Flash检查 | 通用-两系列共用 | CLK,D0-D3共用，Flash1的CS用PA12，Flash2的CS用PA26（PU管脚，适用于低有效的CS） |

## 关联页面
- [[CR_RefDesign_ExternalFlash_Power]]
- [[CR_RefDesign_EMMC_SD_Pullup]]
- [[CR_SDMMC_MPI2_Exclusive]]
- 来源摘要：[[SF32LB52_Checklist_V0.1_20241008]]

## 原始来源完整引用
1. [SF32LB52 Checklist V0.1 20241008]，Raw：raw/mcu/all_chip/design_checklist/SF32LB52_Checklist_V0.1_20241008.md，章节：存储（共 11 条）。

## 待核实问题
- 无（参数来自官方 Checklist 黄金样板）。
