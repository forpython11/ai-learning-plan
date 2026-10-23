# 第 2 周第 1 节：认识特征、标签，并拆分训练集和测试集。

from sklearn.datasets import load_iris  # 导入 Scikit-learn 自带的鸢尾花示例数据。
from sklearn.model_selection import train_test_split  # 导入拆分训练数据和测试数据的工具。

iris = load_iris(as_frame=True)  # 加载 150 朵鸢尾花的数据，并用表格形式保存。
X = iris.data  # 取出四个测量值作为特征 X。
y = iris.target  # 取出花的类别编号作为标签 y。
label_names = dict(enumerate(iris.target_names.tolist()))  # 建立类别编号到花名的对应关系。

print(f"全部特征的列名：{list(X.columns)}")  # 显示模型可以参考的四项特征。
print(f"特征表的形状：{X.shape}（例子数，特征数）")  # 显示共有 150 个例子和 4 项特征。
print(f"标签对应的花名：{label_names}")  # 显示标签编号 0、1、2 各代表哪种花。
print(f"前 5 个标签编号：{y.head().tolist()}")  # 查看前五朵花的已知类别编号。

X_train, X_test, y_train, y_test = train_test_split(  # 把特征和对应标签拆成训练部分与测试部分。
    X, y,  # 同时传入特征和标签，确保每朵花的数据和答案配对。
    test_size=0.2,  # 留出 20% 的例子作为测试集，其余 80% 用于训练。
    random_state=42,  # 固定随机种子，让每次运行都得到同一份拆分结果。
    stratify=y,  # 按类别比例拆分，避免某一种花在某一组里过少。
)  # 结束拆分，并接收四份结果。

print(f"\n训练集特征形状：{X_train.shape}")  # 训练集有 120 朵花，每朵有 4 项特征。
print(f"测试集特征形状：{X_test.shape}")  # 测试集有 30 朵花，每朵有 4 项特征。
print(f"训练集标签数量：{len(y_train)}")  # 显示训练集里有多少个已知答案。
print(f"测试集标签数量：{len(y_test)}")  # 显示测试集里有多少个留待检查的答案。

print("\n训练集中各类花的数量：")  # 打印训练集类别统计的标题。
print(y_train.map(label_names).value_counts().sort_index())  # 把标签编号换成花名后统计数量。
print("\n测试集中各类花的数量：")  # 打印测试集类别统计的标题。
print(y_test.map(label_names).value_counts().sort_index())  # 检查测试集也保留了各类花的样本。
