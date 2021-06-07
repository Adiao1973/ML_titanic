import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 使用RandomForestRegressor填补缺失的年龄属性
def set_miss_ages(df):
    # 把已有的数值型特征取出来丢进RandomForestRegressor中
    age_df = df[['age','pclass','embarked','sex']]

    # 乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.age.notnull()].values
    unknown_age = age_df[age_df.age.isnull()].values

    # y即目标年龄
    y = known_age[:, 0]

    # X即特征属性值
    X = known_age[:, 1:]

    # 建立训练模型并训练
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X, y)

    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])

    # 用得到的预测结果填补原缺失数据
    df.loc[(df.age.isnull()), 'age'] = predictedAges

    return df

titanic = pd.read_csv("Titanic\DataSet\\train\\titanicOut3.csv")

titanic = set_miss_ages(titanic)

# 将Embarked,Sex,Pclass转换成为one-hot编码
dummies_embarked = pd.get_dummies(titanic['embarked'], prefix='embarked')
dummies_sex = pd.get_dummies(titanic['sex'], prefix='sex')
dummies_pclass = pd.get_dummies(titanic['pclass'], prefix= 'pclass')

df = pd.concat([titanic, dummies_embarked, dummies_sex, dummies_pclass], axis=1)
df.drop(['pclass','sex','embarked'], axis=1, inplace=True)

print(df)
df.to_csv("Titanic\DataSet\\train\\titanicOut4.csv", index=False)

# 导入测试集
titanic_test = pd.read_csv("Titanic\DataSet\\test\\testOut.csv")

# 填补缺失的年龄
titanic_test = set_miss_ages(titanic_test)

# 将Embarked,Sex,Pclass转换成为one-hot编码
dummies_embarked = pd.get_dummies(titanic_test['embarked'], prefix='embarked')
dummies_sex = pd.get_dummies(titanic_test['sex'], prefix='sex')
dummies_pclass = pd.get_dummies(titanic_test['pclass'], prefix= 'pclass')

df2 = pd.concat([titanic_test, dummies_embarked, dummies_sex, dummies_pclass], axis=1)
df2.drop(['pclass','sex','embarked'], axis=1, inplace=True)

print(df2)
df2.to_csv("Titanic\DataSet\\test\\testOut2.csv", index=False)