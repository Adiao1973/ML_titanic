import pandas as pd

# 导入数据
titanic = pd.read_csv("Titanic\DataSet\\train\\titanicOut2.csv")

# 将等级舱转化成数值型特征
titanic['pclass'].replace('1st', 1, inplace=True)
titanic['pclass'].replace('2nd', 2, inplace=True)
titanic['pclass'].replace('3rd', 3, inplace=True)

# 将登陆港口转化为数值型特征
titanic['embarked'].replace('Southampton', 1, inplace=True)
titanic['embarked'].replace('Cherbourg', 2, inplace=True)
titanic['embarked'].replace('Queenstown', 3, inplace=True)

# 将性别转化为数值型特征
titanic['sex'].replace('female', 0, inplace=True)
titanic['sex'].replace('male', 1, inplace=True)

# 导出数据
titanic.to_csv("Titanic\DataSet\\train\\titanicOut3.csv",index=False)