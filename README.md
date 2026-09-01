# Boolean Expression Simplification Experiments

离散数学课程加分题中的一组布尔表达式化简实验。题目给出 3、5、10 个变量的真值表，需要构造与目标真值表等价、尽量简洁的合式公式。

这个仓库记录了两种思路：先在受限表达式空间中暴力搜索，随后改为直接分析真值表中的局部结构。后一个版本借用了 Quine–McCluskey 的合并思路，但实现重点是局部真值模式化简。

## 目录

```text
.
├── 1_Bruteforce_Method/
│   ├── bruteforce_3_vars.py
│   ├── bruteforce_5_vars.py
│   └── expression_validator.py
├── 2_Quine_McCluskey_Method/
│   ├── qm_main_solver.py
│   ├── qm_solver_v2.py
│   └── qm_solver_v3.py
├── data/
│   ├── data.csv
│   ├── data5.csv
│   ├── data10.csv
│   └── 真值表.xlsx
├── utils/
└── requirements.txt
```

## 1. 受限空间中的暴力搜索

最早的版本直接枚举候选表达式，并在真值表的每一行上验证其输出。

以 3 变量版本为例，搜索空间由这些因素组成：

- 每个变量使用原变量或其否定形式；
- 变量排列顺序；
- `&` / `|` 运算符组合；
- 固定的括号结构。

候选式通过 Python `eval()` 在所有输入组合上逐行验证。

这里枚举的是预先限定的表达式结构。变量数增加后，排列数和运算符组合数迅速增长，5 变量版本已经出现明显的组合爆炸。

## 2. 从真值表中寻找可合并模式

后续实验位于：

```text
2_Quine_McCluskey_Method/
```

这一版受 Q-M 合并思想启发，直接从真值表中寻找可以合并的局部模式。

`qm_main_solver.py` 的主要过程是：

1. 取出输出为 1 的真值表行；
2. 枚举两个变量 `i, j`；
3. 找出其余变量完全相同的行；
4. 统计这组行在 `i, j` 上出现的二元真值模式；
5. 将模式翻译成更短的逻辑关系；
6. 与其余固定变量重新组合成析取式。

代码能够识别的二元模式包括：

```text
a ∧ b
a ∨ b
a ⊕ b
a ↔ b
a → b
¬a
b
...
```

例如，如果若干输出为 1 的行只在两个变量上变化，而这两个变量的取值组合对应某个熟悉的二元逻辑关系，就可以用该关系代替多项展开。

## 与标准 Quine–McCluskey 的区别

标准 Q-M 算法会对 minterm 反复进行逐层合并，生成 prime implicant，并通过 prime implicant chart 选择覆盖。

本仓库没有实现完整的：

- 多轮 implicant 合并；
- prime implicant 生成；
- prime implicant chart；
- 最小覆盖求解。

所以它更接近一种局部化简方法，不包含标准 Q-M 中的完整最小覆盖过程。

## 版本说明

- `bruteforce_3_vars.py` / `bruteforce_5_vars.py`：早期受限暴力搜索；
- `qm_solver_v2.py` / `qm_solver_v3.py`：开发过程中的实验版本，真值表直接嵌在源码中；
- `qm_main_solver.py`：面向 10 变量数据的主要版本，默认读取 `data/data10.csv`；
- `expression_validator.py`：用于逐行检查一个给定表达式是否与目标真值表一致；
- `utils/`：当时用于表达式格式转换和代码整理的辅助脚本。

## 运行

安装依赖：

```bash
pip install -r requirements.txt
```

当前主脚本只需要 `numpy`：

```bash
python 2_Quine_McCluskey_Method/qm_main_solver.py
```

脚本会从仓库中的 `data/data10.csv` 读取 10 变量真值表，并输出按当前启发式规则得到的表达式。

暴力搜索版本可以直接运行：

```bash
python 1_Bruteforce_Method/bruteforce_3_vars.py
python 1_Bruteforce_Method/bruteforce_5_vars.py
```

## 数据

`data/` 中保留了课程阶段使用过的 3、5、10 变量真值表。部分实验脚本仍将对应真值表直接写在源码中，因此不同版本并不共用统一的数据接口。

## 思路变化

```text
在限定语法空间中枚举候选
                ↓
直接利用真值表中的重复结构做局部合并
```
