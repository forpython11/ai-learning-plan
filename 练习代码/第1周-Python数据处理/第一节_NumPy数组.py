"""第 1 周第 1 节：NumPy 数组与向量化练习。"""

import numpy as np

students = ["林青", "周然", "陈可", "赵宁"]
scores = np.array(
    [
        [88, 92, 79],
        [76, 85, 90],
        [95, 89, 93],
        [60, 72, 68],
    ],
    dtype=float,
)

print(f"数组形状：{scores.shape}（学生数，测验数）")
print(f"第一位学生的成绩：{scores[0]}")
print(f"第二位学生第一次测验：{scores[1, 0]:.0f} 分")

student_averages = scores.mean(axis=1)
quiz_averages = scores.mean(axis=0)

print("\n每位学生的平均分：")
for name, average in zip(students, student_averages):
    print(f"{name}：{average:.1f}")

print(f"\n每次测验的平均分：{quiz_averages.round(1)}")

high_scores = scores[scores >= 90]
print(f"\n90 分及以上的成绩：{high_scores}")
print(f"90 分及以上共 {high_scores.size} 个")

improved_scores = np.minimum(scores + 2, 100)
print(f"\n统一加 2 分并封顶 100 后：\n{improved_scores}")
