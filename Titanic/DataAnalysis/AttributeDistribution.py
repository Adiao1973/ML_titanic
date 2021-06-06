#encoding:utf-8
from numpy import poly
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

fig = plt.figure(figsize=(15, 10))
# 设定图表颜色alpha参数
fig.set(alpha=0.2)

plt.subplot2grid((2, 3), (0, 0))
titanic.survived.value_counts().plot(kind='bar')
plt.title("获救情况（1为获救）")
plt.ylabel("人数")

plt.subplot2grid((2, 3), (0, 1))
titanic.pclass.value_counts().plot(kind="bar")
plt.ylabel("人数")
plt.title("乘客等级分布")

plt.subplot2grid((2, 3), (0, 2))
plt.scatter(titanic.survived, titanic.age)
plt.ylabel("年龄")
plt.grid(b=True, which='major', axis='y')
plt.title("按年龄看获救分布（1为获救）")

plt.subplot2grid((2, 3), (1, 0), colspan=2)
titanic.age[titanic.pclass == '1st'].plot(kind='kde')
titanic.age[titanic.pclass == '2nd'].plot(kind='kde')
titanic.age[titanic.pclass == '3rd'].plot(kind='kde')
plt.xlabel("年龄")
plt.ylabel("密度")
plt.title("各等级的乘客年龄分布")
plt.legend(('头等舱', '一等舱', '三等舱'), loc='best')

plt.subplot2grid((2, 3), (1, 2))
titanic.embarked.value_counts().plot(kind='bar')
plt.title("各登船口岸上船人数")
plt.ylabel("人数")
plt.show()