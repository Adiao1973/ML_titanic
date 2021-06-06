import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

#查看起始到目的点的获救情况
fig = plt.figure()
# 设定图表颜色alpha参数
fig.set(alpha=0.2)

Surived_0 = titanic.homedest[titanic.survived == 0].value_counts()
Surived_1 = titanic.homedest[titanic.survived == 1].value_counts()

df = pd.DataFrame({'获救':Surived_1,'未获救': Surived_0})
df.plot(kind='bar',stacked=True)
plt.title("不同起始点目的点乘客的获救情况")
plt.xlabel("起始目的点")
plt.ylabel("人数")

plt.show()
