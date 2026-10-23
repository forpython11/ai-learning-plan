# 第二节：Pandas 读取与分析 CSV

## 本节目标

- 用 Pandas 把 CSV 读成表格；
- 查看行列、列名和数据类型；
- 选择列、筛选记录并计算总额；
- 按类别分组汇总，再导出 CSV。

## 1. 安装与运行

在项目根目录安装 Pandas：

```powershell
# 在项目虚拟环境中安装 Pandas。
.\.venv\Scripts\python.exe -m pip install pandas
```

运行本节练习：

```powershell
# 用项目虚拟环境运行第二节练习。
.\.venv\Scripts\python.exe .\练习代码\第1周-Python数据处理\第二节_Pandas读取CSV.py
```

## 2. 把 CSV 读成表格

```python
import pandas as pd  # 导入 Pandas，并把它简称为 pd。

df = pd.read_csv("消费记录.csv")  # 读取 CSV 文件，并把表格放进 df。
print(df.head())  # 显示表格的前五行。
print(df.shape)  # 显示表格的行数和列数。
print(df.dtypes)  # 显示每一列的数据类型。
```

这里的 `df` 是一个 DataFrame，可以把它先理解成带行列标签的表格。`shape` 返回「行数、列数」；`dtypes` 显示每一列的数据类型。

## 3. 选择、筛选和计算

```python
amounts = df["金额"]  # 取出“金额”这一列。
large_spends = df[df["金额"] >= 50]  # 筛选出金额不低于 50 的记录。
total = df["金额"].sum()  # 把金额列中的数字相加。
```

`df["金额"]` 选择一列；`df[条件]` 保留满足条件的行；`sum()` 汇总金额。

## 4. 分组汇总与导出

```python
summary = df.groupby("类别")["金额"].agg(["sum", "mean"]).round(2)  # 分组计算总额和平均金额，并保留两位小数。
summary.to_csv("分类汇总.csv", index_label="类别", encoding="utf-8-sig")  # 将汇总表保存为 CSV 文件。
```

`groupby("类别")` 按类别分组；`agg` 同时计算总额和平均值。`index_label` 给导出文件中的索引列命名，`utf-8-sig` 便于用 Excel 打开中文 CSV。

## 本节练习

先在运行代码前写下你的预测，再运行核对：

1. 增加一条「学习」类别的 20 元消费，重新计算总支出。
2. 筛选金额大于等于 30 元的消费，数一数有几条。
3. 把分组统计改成只算平均金额，比较哪一类平均消费最高。
4. 把一条记录的金额暂时留空，观察 `df["金额"].isna().sum()` 的结果。思考：未知金额应该直接当作 0 吗？
