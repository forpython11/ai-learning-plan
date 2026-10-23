# 第 1 周第 3 节：从消费 CSV 统计数据并画图。

from pathlib import Path  # 导入路径工具，用来定位输入和输出文件。

import matplotlib.pyplot as plt  # 导入 Matplotlib 的绘图接口，并简称为 plt。
import pandas as pd  # 导入 Pandas，用它读取和整理 CSV 表格。

data_path = Path(__file__).with_name("消费记录.csv")  # 找到脚本旁边的消费数据文件。
output_path = Path(__file__).with_name("消费分析图.png")  # 设置图片要保存的位置和文件名。
df = pd.read_csv(data_path)  # 把 CSV 文件读成 Pandas 表格。
category_totals = (  # 开始计算每个类别的消费总额。
    df.groupby("类别")["金额"]  # 按类别分组，然后选出每组的金额列。
    .sum()  # 把每个类别里的金额相加。
    .sort_values(ascending=False)  # 按总额从高到低排序。
)  # 结束类别汇总计算。
daily_totals = df.groupby("日期")["金额"].sum().sort_index()  # 按日期计算每天的消费总额。

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]  # 设置中文字体候选项。
plt.rcParams["axes.unicode_minus"] = False  # 让坐标轴上的负号正常显示。
fig, (category_axis, daily_axis) = plt.subplots(1, 2, figsize=(12, 5))  # 创建一行两列的画布和两张图。

category_axis.bar(category_totals.index, category_totals.values, color="#ffaa11")  # 画出各类别的消费总额柱状图。
category_axis.set_title("各类别消费总额")  # 设置左图标题。
category_axis.set_xlabel("类别")  # 设置左图横轴名称。
category_axis.set_ylabel("金额（元）")  # 设置左图纵轴名称。
category_axis.grid(axis="y", alpha=0.25)  # 添加浅色横向网格，方便比较金额。

daily_axis.plot(daily_totals.index, daily_totals.values, marker="o", color="#d97745")  # 画出每日消费折线图。
daily_axis.set_title("每日消费总额")  # 设置右图标题。
daily_axis.set_xlabel("日期")  # 设置右图横轴名称。
daily_axis.set_ylabel("金额（元）")  # 设置右图纵轴名称。
daily_axis.tick_params(axis="x", rotation=35)  # 旋转日期标签，避免标签挤在一起。
daily_axis.grid(axis="y", alpha=0.25)  # 添加浅色横向网格，方便比较金额。

fig.tight_layout()  # 自动调整两张图之间的间距。
fig.savefig(output_path, dpi=160)  # 把图表保存成 PNG 图片。
print(f"图表已保存：{output_path}")  # 显示图片保存路径。
plt.close(fig)  # 关闭绘图对象，让终端脚本保存图片后正常结束。
