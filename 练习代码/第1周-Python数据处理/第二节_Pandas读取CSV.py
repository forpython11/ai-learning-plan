# 第 1 周第 2 节：读取和分析消费 CSV。

from pathlib import Path  # 导入路径工具，用来定位脚本旁边的 CSV 文件。

import pandas as pd  # 导入 Pandas，并在后面用 pd 作为它的简称。

data_path = Path(__file__).with_name("消费记录.csv")  # 找到与本脚本同一文件夹里的输入数据。
output_path = Path(__file__).with_name("分类汇总.csv")  # 设置汇总结果要保存到的文件路径。

df = pd.read_csv(data_path)  # 读取 CSV 文件，并把表格保存到 DataFrame 变量 df。

print("前 5 条记录：")  # 打印下面内容的标题。
print(df.head().to_string(index=False))  # 显示前五行，并隐藏 Pandas 自带的行号。
print(f"\n表格形状：{df.shape}（记录数，字段数）")  # 显示总行数和总列数。
print(f"总支出：{df['金额'].sum():.2f} 元")  # 取出金额列求和，并保留两位小数。

category_summary = (  # 开始创建按类别统计的汇总表。
    df.groupby("类别")["金额"]  # 先按类别分组，再取每组的金额列。
    .agg(["sum", "mean"])  # 同时计算每组的总额和平均金额。
    .round(2)  # 把统计结果四舍五入到两位小数。
    .sort_values("sum", ascending=False)  # 按总额从高到低排列类别。
)  # 结束这一组连续的数据处理操作。
category_summary.columns = ["总额", "平均金额"]  # 把英文统计列名改成中文。

print("\n按类别汇总：")  # 打印汇总表的标题。
print(category_summary.to_string())  # 把完整汇总表打印出来。

large_spends = df[df["金额"] >= 50]  # 只保留金额不低于 50 元的记录。
print("\n金额不低于 50 元的记录：")  # 打印筛选结果的标题。
print(large_spends.to_string(index=False))  # 显示筛选出的行，并隐藏行号。

category_summary.to_csv(  # 把汇总表写入一个 CSV 文件。
    output_path,  # 使用前面设置好的输出文件路径。
    index_label="类别",  # 给索引列命名为“类别”。
    encoding="utf-8-sig",  # 使用适合 Excel 打开中文内容的编码。
)  # 结束保存操作。
print(f"\n汇总文件已保存：{output_path.name}")  # 显示生成的文件名。

# 第 1 题：在表格最后增加一笔 20 元的学习消费。
df.loc[len(df)] = {
    "日期": "2026-10-08",  # 新记录的日期。
    "类别": "学习",  # 新记录的类别。
    "金额": 20,  # 新记录的金额。
    "说明": "打印资料",  # 新记录的说明。
}
# 重新计算包含新记录的总支出。
print(f"总支出：{df['金额'].sum():.2f} 元")  # 当前示例数据下结果是 478.70 元。

# 第 2 题：筛选金额不低于 30 元的消费记录。
records_over_30 = df[df["金额"] >= 30]  # 条件为真的行会保留下来。
print(f"记录数：{len(records_over_30)}")  # 当前示例数据下结果是 7 条。

# 第 3 题：按类别计算平均金额，并从高到低排列。
average_by_category = (
    df.groupby("类别")["金额"]  # 按类别分组，再选金额列。
    .mean()  # 计算每个类别的平均金额。
    .sort_values(ascending=False)  # 按平均金额从高到低排序。
    .round(2)  # 结果保留两位小数。
)

print(average_by_category, "按平均金额从高到低排序")  # 当前数据下餐饮略高于学习，分别约为 37.80 和 37.78 元。

# 第 4 题：把第一条记录的金额临时设为空。
df.loc[0, "金额"] = pd.NA  # 这里只修改内存中的表格，不会修改原 CSV。
print(df["金额"].isna().sum())  # 统计金额为空的行数，结果是 1。
