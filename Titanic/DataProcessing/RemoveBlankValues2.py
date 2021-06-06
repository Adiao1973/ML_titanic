import pandas as pd

# 导入数据
titanic = pd.read_csv("Titanic\DataSet\\train\\titanicOut4.csv.csv")

# 删除用不了的数据的列
titanic.drop(['name','homedest'],axis=1,inplace=True)

# 导出数据
titanic.to_csv("Titanic\DataSet\\train\\titanicOut5.csv",index=False)
