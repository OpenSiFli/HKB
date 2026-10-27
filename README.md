# HKB —— SiFli 硬件知识库（Hardware Knowledge Base）

> 本仓库是 SiFli（思澈科技）MCU 硬件知识的**文档源仓库**，基于 Sphinx 构建，自动部署至 `docs.sifli.com/projects/HKB`。
> 内容沉淀自内部硬件知识库（Obsidian 双链知识库），面向硬件工程师，提供 SiFli 全系列 MCU 与开发板的硬件设计、审查与选型参考。

---

## 一、仓库定位

HKB（Hardware Knowledge Base）系统整理 SiFli 全系列 MCU 与开发板的硬件知识，目标是把分散在规格书、用户手册、硬件设计指南、参考设计、官方 Checklist、AVL 物料清单与工程复盘中的关键信息，结构化沉淀为可检索、可审图、可复用的知识资产。

知识库按两大平级类别组织：

- **MCU 全系列硬件知识库**（`wiki/mcu/`）—— 以芯片实体为核心，覆盖外设、引脚复用、硬件设计指南、参考设计、审图规则、设计规范、故障案例、AVL 物料库。
- **开发板（Dev Board）硬件知识库**（`wiki/dev_board/`）—— 以原理图为主要入库依据，提取开发板核心参数并与 MCU 知识库双向双链。

---

## 二、内容结构

### 1. MCU 全系列硬件知识库

#### 已覆盖芯片家族（两大家族，各含两个独立系列，不可合并看待）

| 家族 | 系列 | 供电特征 |
| --- | --- | --- |
| **SF32LB52** | `SF32LB52X`（大写 X）= 3.3V 供电系列 | 无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电 |
| | `SF32LB52x`（小写 x）= 电池供电系列 | 内置 560mA 充电，电源引脚 VBUS/VBAT/VCC |
| **SF32LB57** | `SF32LB57X`（大写 X）= 3.3V 供电系列 | 无充电电路，主电 PVDD，GPIO 由 VDDIOA 供电 |
| | `SF32LB57x`（小写 x）= 电池供电系列 | 内置充电模块，电源引脚 VBUS/VBAT/VCC/VSYS |

> 📌 文档标题大小写与芯片系列**一致**：3.3V 系列用大写 X（如 DS5202-SF32LB52X），电池系列用小写 x（如 DS5201-SF32LB52x）。

#### 知识维度

- **芯片实体（chip_entity）**：封装、引脚、电气参数、极限规格、典型电路、约束禁忌、勘误、原厂/企业规范。
- **外设专项（peripheral）**：GPIO / 电源 / 时钟 / GPADC / 音频 / 蓝牙射频 / 串口（UART-I2C-SPI-CAN）/ 存储（MPI-SD-eMMC）/ 定时器 PWM / 显示与图形（ePicasso·LCD·DCMI·eZip）等。
- **引脚复用矩阵（PINMUX）**：大核 GPIO 完整复用总表 + matrix index + LCD mux；以官方 xlsx 为权威依据，并标注与规格书差异。
- **硬件设计指南（Hardware Design Guide）**：官方 wiki 硬件设计指南，3.3V 系列与电池系列各一份，含封装 / 典型方案 / 原理图 / PCB 设计（叠层·走线·EMI/ESD）全章节。
- **参考设计原理图（Reference Schematic）**：官方参考设计结构化提炼（黄金样板），含电源架构 / 关键 BOM / 设计要点与对应审图规则。
- **校验规则（Check Rules / `CR_*`）**：源自规格书、用户手册、参考设计与官方 Checklist 的审图规则，覆盖多电源域、绝对最大额定值、EPAD 接地、低功耗浮空 IO、48M/32K 晶振、BLE 天线、USB 差分对、复位电平、BOOT 寄存器、I2C 总线卡死、存储互斥、接口电平匹配、电池 OVP/电源树等。
- **设计规范（Design Rules / `DR_*`）**：电源架构、GPIO 默认 PUPD 高阻、低功耗 IO 保持、复位设计、调试接口、BOOT 模式、PA34 电源键引脚作普通 GPIO 使用等。
- **故障案例（Fault Cases / `FC_*`）**：I2C 总线卡死、调试接口失效、Hibernate 合封漏电、SDMMC-FIFO 溢出等工程复盘。
- **AVL 合格物料库**：SiFli 官方 AVL 认证物料清单（晶体 / Buck 电感 / Nor Flash / SPI Nand / SD Nand / LCD 驱动），BOM 选型优先级高于器件原厂规格书，覆盖**全系列 SIFLI MCU**。

### 2. 开发板（Dev Board）硬件知识库

以原理图为主要入库依据，提取开发板 11 项核心参数（平台 / 芯片 / 模组 / 上芯方式 / 存储配置 / 供电方式 / 外设 / 调试接口 / 适用场景 / 使用指南文档 / 图纸），与 MCU 知识库单向引用（不修改 MCU 侧文件）。

### 3. 原始资料（Raw）与来源摘要

- 规格书 / 勘误 / 内部一致性核查报告
- 官方硬件 Checklist、硬件设计指南 PDF、参考设计 / PCB / BOM
- 企业规范 / 报告模板、故障复盘原始资料
- 每份原始资料对应一份来源摘要页（`sources/`），永久保留双链。

---

## 三、文档构建

本仓库使用 SiFli 官方文档工具链 `sifli-docs-toolbox` 构建中英双语文档：

```shell
pip install -r requirements.txt
sf-build-docs --lang zh_CN --version latest
sf-build-docs --lang en     --version latest
```

- 文档源位于 `source/`（按 `zh_CN` / `en` 分语言）。
- 部署地址与版本由 `.github/workflows/build-docs.yml` 中的 `PROJ_NAME` 控制（当前为 `HKB`），版本号列表见 `version.json`。
- CI 默认 `workflow_dispatch` 手动触发（push 触发已注释关闭）。

> 说明：当前 `source/` 下的示例模板内容已清理，正式知识库文档正在从内部知识库迁移填充中。

---

## 四、相关资源

- SiFli 官网：<https://www.sifli.com/>
- 芯片选型与开发板 Wiki（中文 / English）：<https://wiki.sifli.com/> 、<https://wiki.sifli.com/en/>
- SDK 文档：<https://docs.sifli.com/>
- SiFli SDK（GitHub）：<https://github.com/OpenSiFli/SiFli-SDK>
- 官方论坛（BBS）：<https://bbs.sifli.com/>
- 商务联系：sales@sifli.com

---

## 五、License

本仓库文档采用 **Apache License 2.0**，详见 [LICENSE](./LICENSE)。
