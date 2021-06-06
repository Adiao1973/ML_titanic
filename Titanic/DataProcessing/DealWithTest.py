import pandas as pd

# 导入测试集
titanic_test = pd.read_csv("Titanic\DataSet\\test\\test.csv")

# 处理测试集
# 删除关联不大的列
titanic_test.drop(['Name','SibSp','Parch','Ticket','Fare','Cabin'], axis=1, inplace=True)

# 将性别转化为数值型特征
titanic_test['Sex'].replace('female', 0, inplace=True)
titanic_test['Sex'].replace('male', 1, inplace=True)

# 将登陆港口转化为数值型特征
titanic_test['Embarked'].replace('S', 1, inplace=True)
titanic_test['Embarked'].replace('C', 2, inplace=True)
titanic_test['Embarked'].replace('Q', 3, inplace=True)

# 改变列名称
titanic_test = titanic_test.rename(columns={'PassengerID':'row.names','Pclass':'pclass','Sex':'sex','Age':'age','Embarked':'embarked'})

# 导出测试集
titanic_test.to_csv("Titanic\DataSet\\test\\testOut.csv", index=False)