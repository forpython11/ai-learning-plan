# 第一节：NumPy 数组与向量化

## 本节目标

- 用 NumPy 创建二维数组，读懂数组的形状和数据类型；
- 用索引取出一行或一个值；
- 用 `axis` 沿行或列计算；
- 用向量化运算和布尔条件处理整组数据。

## 1. 安装与运行

在项目根目录使用项目虚拟环境安装 NumPy：

```powershell
.\.venv\Scripts\python.exe -m pip install numpy
```

然后用同一个解释器运行练习：

```powershell
.\.venv\Scripts\python.exe .\练习代码\第1周-Python数据处理\第一节_NumPy数组.py
```

## 2. 数组、形状和索引

```python
import numpy as np

scores = np.array([
    [88, 92, 79],
    [76, 85, 90],
    [95, 89, 93],
    [60, 72, 68],
])

print(scores.shape)  # 4 名学生，3 次测验
print(scores[0])     # 第一名学生的全部成绩
print(scores[1, 0])  # 第二名学生第一次测验的成绩
```

二维数组用 `[行, 列]` 定位。索引从 0 开始。数组的 `shape` 描述每个维度的长度。

## 3. 按行列计算

```python
student_averages = scores.mean(axis=1)
quiz_averages = scores.mean(axis=0)
```

`axis=1` 沿每一行计算，得到每位学生的平均分；`axis=0` 沿每一列计算，得到每次测验的平均分。

## 4. 向量化和条件筛选

```python
improved_scores = np.minimum(scores + 2, 100)
high_scores = scores[scores >= 90]
```

第一行一次性给所有成绩加 2 分，并用 100 封顶。第二行选出所有不低于 90 分的成绩。这类整组运算通常比手动逐项循环更简洁。

## 本节练习

1. 给数组增加一位学生的成绩 `[84, 78, 91]`，重新计算每位学生的平均分。
2. 统计总共有多少个成绩不低于 90 分。
3. 将每次测验的平均分四舍五入到 1 位小数。
4. 说出 `scores.shape`、`axis=0` 和 `axis=1` 在这个例子中的含义。
