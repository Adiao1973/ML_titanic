import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

#查看各登录港口的获救情况
fig = plt.figure()
# 设定图表颜色alpha参数
fig.set(alpha=0.2)

Survived_0 = titanic.embarked[titanic.survived == 0].value_counts()
Survived_1 = titanic.embarked[titanic.survived == 1].value_counts()

df = pd.DataFrame({'获救': Survived_1,'未获救': Survived_0})
df.plot(kind = 'bar', stacked = True)
plt.title("各登录港口乘客的获救情况")
plt.xlabel("登录港口")
plt.ylabel("人数")

plt.show()