import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier

# 导入数据集
titanic = pd.read_csv("Titanic\DataSet\\train\\titanicOut5.csv")

# 将数据的标签分离出来
train_label = titanic['survived']
train_titanic = titanic.drop('survived', 1)

# 对数据进行模型预测
rfc = RandomForestClassifier(random_state=1, n_estimators=12, min_samples_split=2, min_samples_leaf=1)
kf = model_selection.KFold(n_splits=3, shuffle=False, random_state=None)
scores = model_selection.cross_val_score(rfc, train_titanic, train_label, cv=kf)

print(scores.mean())