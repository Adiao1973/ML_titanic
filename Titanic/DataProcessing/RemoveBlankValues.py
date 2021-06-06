import pandas as pd

# 导入数据
titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

# 删除空白数据
titanic.dropna(subset=['embarked','homedest'],inplace=True)

# 删除缺少数据过多的列
titanic.drop(['room','ticket','boat'],axis=1,inplace=True)

# 导出数据
titanic.to_csv("Titanic\DataSet\\train\\titanicOut2.csv",index=False)
