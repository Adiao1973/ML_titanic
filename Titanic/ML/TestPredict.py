import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 导入测试集
df_test = pd.read_csv("Titanic\DataSet\\test\\testOut2.csv")

# 导入训练集
titanic = pd.read_csv("Titanic\DataSet\\train\\titanicOut5.csv")

# 将数据的标签分离出来
train_label = titanic['survived']
train_titanic = titanic.drop('survived', 1)

# 先用训练集上的数据训练出一个模型，再在测试集上进行预测，并将结果输出到一个csv文件中
model = RandomForestClassifier(random_state=1, n_estimators=12, min_samples_split=2, min_samples_leaf=1)
model.fit(train_titanic, train_label)
predictions = model.predict(df_test)
result = pd.DataFrame({'PassengerId':df_test['row.names'].values,'Survived': predictions.astype(np.int32)})
result.to_csv("Titanic\DataSet\\result\prediction.csv", index=False)
print(pd.read_csv("Titanic\DataSet\\result\prediction.csv"))