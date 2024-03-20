import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# load dataset
data_path = 'dataset/spambase/spambase.data'  
data = pd.read_csv(data_path, header=None)

# 数据集最后一列是标签（1表示垃圾邮件，0表示非垃圾邮件）
X = data.iloc[:, :-1]  # 特征
y = data.iloc[:, -1]   # 标签

# 可选：标准化特征
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 显示划分后的数据集大小
print(f'Training set size: {X_train.shape[0]} samples')
print(f'Test set size: {X_test.shape[0]} samples')

# 检查数据集中是否有缺失值
missing_values = data.isnull().sum()
print("缺失值数量：\n", missing_values)
