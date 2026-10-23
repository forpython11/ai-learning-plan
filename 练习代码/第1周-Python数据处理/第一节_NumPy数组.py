# 第 1 周第 1 节：NumPy 数组与向量化练习。

import numpy as np  # 导入 NumPy，并在后面用 np 作为它的简称。

students = ["林青", "周然", "陈可", "赵宁"]  # 保存每一行成绩对应的学生姓名。
scores = np.array(  # 把下面的成绩数据转换成 NumPy 数组。
    [
        [88, 92, 79],  # 第一名学生三次测验的成绩。
        [76, 85, 90],  # 第二名学生三次测验的成绩。
        [95, 89, 93],  # 第三名学生三次测验的成绩。
        [60, 72, 68],  # 第四名学生三次测验的成绩。
    ],
    dtype=float,  # 使用小数类型，方便后面保存平均分。
)  # 结束数组创建。

print(f"数组形状：{scores.shape}（学生数，测验数）")  # 显示行数和列数。
print(f"第一位学生的成绩：{scores[0]}")  # 用索引 0 取出第一行。
print(f"第二位学生第一次测验：{scores[1, 0]:.0f} 分")  # 取第二行第一列，并显示为整数。

student_averages = scores.mean(axis=1)  # 按行求平均，得到每位学生的平均分。
quiz_averages = scores.mean(axis=0)  # 按列求平均，得到每次测验的平均分。

print("\n每位学生的平均分：")  # 打印标题；\n 会先换到新的一行。
for name, average in zip(students, student_averages):  # 把姓名和对应平均分逐个配对。
    print(f"{name}：{average:.1f}")  # 每次循环打印一位学生的姓名和平均分。

print(f"\n每次测验的平均分：{quiz_averages.round(1)}")  # 把测验平均分四舍五入到一位小数。

high_scores = scores[scores >= 90]  # 用条件筛选出所有不低于 90 分的单次成绩。
print(f"\n90 分及以上的成绩：{high_scores}")  # 显示筛选出的成绩。
print(f"90 分及以上共 {high_scores.size} 个")  # size 是筛出的成绩数量，不是学生人数。

improved_scores = np.minimum(scores + 2, 100)  # 所有成绩加 2 分，并把超过 100 的分数限制为 100。
print(f"\n统一加 2 分并封顶 100 后：\n{improved_scores}")  # 显示调整后的整张成绩表。

scores = np.vstack([scores, [84, 78, 91]])  # 把新同学的三次成绩作为一行加到数组末尾。
students.append("新同学")  # 在姓名列表末尾添加与新成绩对应的名字。

print(scores.mean(axis=1).round(1), "新增学生后的每人平均分")  # 重新计算五位学生的平均分。
print(np.count_nonzero(scores >= 90), "90 分及以上的单次成绩个数")  # 统计所有测验成绩中不低于 90 分的个数。
