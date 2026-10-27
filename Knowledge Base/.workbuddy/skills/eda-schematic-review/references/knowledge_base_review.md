# 知识库评审流程参考（SF32LB52X 系列 MCU 原理图审图）

本文件供 `eda-schematic-review` 技能调用，记录从「提取结构化文本」到「对照知识库校验规则出报告」
的完整流程、关键坑点与环境约定。本文件随技能存放在 `.workbuddy/skills/eda-schematic-review/references/`，
与知识库一起拷贝即可复用，**不含任何机器专属绝对路径**。

## 0. 环境约定（跨机器可移植）

- **Python**：需要一个含 `pdfplumber` 与 `fpdf2` 的 Python 3 解释器。
  推荐在本机建独立 venv（与知识库一起拷贝即可复用，避免污染全局环境）：
  `<python3> -m venv venv && venv/Scripts/pip install pdfplumber fpdf2`，
  之后用 `venv/Scripts/python.exe` 运行 `scripts/` 下脚本。**不要硬编码某台机器的解释器绝对路径**。
- **中文字体**：`scripts/md2pdf_report.py` 默认自动探测 Windows 中文字体
  （`msyh.ttc` → `simsun.ttc` → `simhei.ttf`），均不存在时明确报错并提示用 `--font` 指定。
  非 Windows 或缺少中文字体时，传入一个支持中文的 TTF/TTC 即可。
- **报告状态符号禁用 emoji**：msyh 等常见中文字体不含 ✅/🔴/🟡/➖/✓/↔ 等字形，转 PDF 后会变成空白方框。
  状态一律用纯文字：**通过 / 命中 / 待核实 / N/A**（必要时附英文 PASS/Hit）。
- **图片不可见**：当前模型无法读取渲染出的 PNG/DWG 栅格图（Read 返回内容过滤）。
  因此**禁止依赖视觉核对布线**，一律改用「矢量文本坐标 + 全文检索」还原电路。
- **方案A 合并文本歧义 → 坐标级消歧**：方案A 将同一水平行的文本合并为一行、并记录该行「一个代表坐标」。
  这会**把相邻/跨元件位号归并并采用边缘坐标**，造成元件归属误判——
  实例：WS501 的 `C324` 被与同行 `LP5308QVF` 充电器合并为一行并记录充电器侧坐标，
  误导 v3 误判" C324 属 LP5308 充电器、非晶体负载电容"（实为 Y300 两端负载电容、双双 DNP）。
  **凡涉及"某元件是否在 X 旁 / 属于哪个模块"的判读，必须用 `scripts/probe_component.py`
  按坐标精确定位目标周边单词复核**，勿凭合并文本单条字符串下结论。
  用法：`python probe_component.py --pdf <input.pdf> --target <Y300|C324|AW3512> [--padx 200] [--pady 170] [--page 3]`。

## 1. 评审前置：判定 MCU 型号与版本（最关键）

型号判定错误会直接推翻整份报告的结论。SF32LB52X 有两个分支，**引脚定义差异巨大**：

- **常规版（52A/52B/52D）**：pin23 = `VDD_SIP`（外部 1.8V 输入）；需外部 32.768kHz 晶振；VBATS 必接。
- **锂电版（523/525/527）**：内部集成 ~560mA 充电器 + Buck/LDO；
  - pin23 = `VDD18_VOUT`（内部 1.8V LDO **输出**，非外部输入）；
  - 内部 RC 可作 RTC 时钟，外部 32.768kHz 晶振**可选**；
  - 电源域：VCC(电池) → 内部 → VSYS / VDD33_VOUT1 / VDD33_VOUT2 / VDD18_VOUT。

判定方法：从提取文本中找充电器芯片（如 AW32012）、电池网络（VBAT/BAT）、`VDD18_VOUT` 字样、
`VSYS` 出处。若图中有外置充电器 + 电池，基本可判定为锂电版。

> 实例：WS501 主板曾误判为常规版，导致「缺 32.768kHz 晶振 / 22pF 负载电容过大 / VBUS_ADC 分压比」三条
> 「关键」结论全部错误。重判定为 **SF32LB525 锂电版** 后这些项被推翻或降级。

## 2. 校验规则（CR_*，共 38 条，分三类）

规则文件位于知识库 `wiki/mcu/all/check_rules/CR_*.md`（路径**相对知识库根目录**，随知识库一起拷贝），
每条含「触发条件 / 风险等级 / 数据手册页码引证」。对照时逐条给出状态之一：PASS / 命中 / 待核实 / N/A（不适用）。

### 2.1 通用 CR_*（18 条，四级风险）

致命（Fatal）：CR_PowerDomains、CR_AbsMaxRatings、CR_EPAD_GND、CR_ATIM_Break_BKIN
严重（Critical）：CR_XTAL48M、CR_BootMode_Register、CR_VBATS_Range、CR_Hibernate_SiP_Supply、
CR_I2C_BusStuck、CR_USB_DPDM、CR_SDMMC_MPI2_Exclusive、CR_Reset_Levels
一般（General）：CR_Reset_PWRKEY、CR_GPADC_SourceResistance、CR_GPIO_Default_PUPD、CR_FloatingIO_LowPower
优化建议（Suggestion）：CR_DebugInterface_PA18_PA19、CR_BLE_RF_Antenna

### 2.2 参考设计黄金样板 CR_RefDesign_*（7 条）

源自官方参考设计原理图，覆盖锂电版关键架构：CR_RefDesign_Batt_OVP_Charger、CR_RefDesign_Batt_PowerTree、
CR_RefDesign_ExternalFlash_Power、CR_RefDesign_Interface_VoltageMatch、CR_RefDesign_XTAL32K、
CR_RefDesign_EMMC_SD_Pullup、CR_RefDesign_LCD_FPC_EMI。

### 2.3 官方硬件 Checklist 转化 CR_Checklist_*（13 条）

由 SiFli 官方硬件 Checklist V0.1 转化，按主题分：电源 / 时钟 / 存储 / 射频 / 显示 / 接口 /
唤醒 / ESD / 生产 / 封装 / 功耗 / 调试 / 音频（文件名见 `wiki/mcu/all/check_rules/CR_Checklist_*.md`）。
接口类（按键/UART/I2C/SPI/GPADC/USB）与电源类是投板前最常命中项。

## 3. 高频真问题模板（投板前必须闭环）

1. **CR_XTAL48M**：48MHz 源两端负载电容标 `DNP` → 须确认晶振料号（石英需焊负载电容，陶瓷谐振器可 DNP）。
   （`DNP` 含义与预留器件判读见 §6。）
2. **CR_I2C_BusStuck**：I²C/SMBus 总线（SCL/SDA）在 MCU 侧与器件侧均**无外部上拉** → 补 2.2k–10kΩ 到 3.3V。
3. **CR_AbsMaxRatings**：5V 信号（VBUS/充电器中断 INT）须确认未直连 MCU GPIO，开漏 INT 上拉到 3.3V 而非 5V。
4. **CR_BootMode_Register**：BOOT 由 `HPSYS_CFG.BMR[0]` 寄存器控制，而非纯外部 strapping；量产固件须置 `BMR[0]=0`。
5. **CR_GPADC_SourceResistance**：分压等效源阻 ≤100kΩ 时，12-bit 采样时间须 ≥300 TPCLK（核对数据手册 Table 4-19）。

## 4. 报告结构（按评审模式分化）

报告章节须服从 SKILL.md「评审模式」一节：**训练模式**含「评审方法与数据源」整节；**正式评审模式**删除该节，
且 checklist 不区分历史版本（直接枚举当前 `wiki/mcu/all/check_rules/CR_Checklist_*.md` 全部条目）。

- **训练模式**：摘要 → 评审方法与数据源 → CR 命中总览表（按 2.1/2.2/2.3 三类展开）→ 风险分级详情 → 投板前待闭环清单（checkbox）→ 结论 → 关联页面/原始来源。
- **正式评审模式**：摘要 → CR 命中总览表（按 2.1/2.2/2.3 三类展开，checklist 用当前总条目、不写历史版本）→ 风险分级详情 → 投板前待闭环清单（checkbox）→ 结论 → 关联页面/原始来源。

完成后用 `scripts/md2pdf_report.py` 转 PDF。

## 5. 全文检索技巧（还原电路、确认引脚是否连接）

对提取出的 `schematic_struct_text.txt` 或原始 PDF 做全文 grep，确认关键点：

- 某引脚/网络是否出现：`grep -n "VDD_SIP\|VBATS\|PA21\|PA34" schematic_struct_text.txt`
- 某元件参数 / 是否预留：`grep -n "DNP\|NC\|NF\|C323\|C324" ...`
- 若 grep 全图空 → 该信号在原理图中确实未连接（据此判 N/A）。

## 6. 元件属性判读：DNP / NC / NF / 灰色 = 预留不焊接

原理图中部分器件被明确标记为「不焊接 / 不装配」，属预留设计（design reserve）。识别这些是避免误判「缺件 / 开路」的前提。
**任一标记出现，均表示该器件在本版本为预留、不焊接（Not Mounted）**：

| 标记 | 含义 | 说明 |
| --- | --- | --- |
| `DNP` | Do Not Populate / 不焊接 | 最通用，BOM 中列为不贴装 |
| `NC` | No Connect / 不连接 | 亦用于「引脚不连接」；元件标 NC 即不装配 |
| `NF` | Not Fitted / 不安装 | 与 DNP 同义，部分厂商 / 图纸习惯用法 |
| 灰色（立创EDA / LCEDA）| 未放置 / 未启用 | 立创EDA 在原理图或 PCB 中将器件标记为灰色（"不放置"状态），等价于 DNP，不在该版本装配 |

**对审图的影响**：
- 提取元件时，凡属性含 DNP / NC / NF 或立创EDA 灰色器件，一律按「未装配」处理；建议在 `extract_A.json` 记录 `status: "DNP"` 以便与已焊接器件区分。
- 对照 CR_* 规则时：若某条规则的被核查对象（如上拉电阻、负载电容、ESD 器件）标 DNP，则该规则对其实例判 **N/A（不适用）**，并在报告中注明「预留不焊」；**切勿当作已焊接电路去判定违规或判缺件**。
- 例：CR_XTAL48M 中 48MHz 晶振两端负载电容标 DNP → 须结合实际料号判断（石英晶体需焊负载电容、陶瓷谐振器可 DNP），不能简单判「缺电容」。
