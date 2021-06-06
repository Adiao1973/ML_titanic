import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.reshape.reshape import stack

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

#乘客舱的等级的获救情况
fig = plt.figure(figsize=(0, 0))
# 设定图表颜色alpha参数
fig.set(alpha=0.2)

# 未获救人数
Surived_0 = titanic.pclass[titanic.survived == 0].value_counts()
# 获救人数
Surived_1 = titanic.pclass[titanic.survived == 1].value_counts()
df = pd.DataFrame({
    '获救': Surived_1,
    '未获救': Surived_0
}).plot(kind='bar', stacked=True)
plt.title("各乘客等级的获救情况")
plt.xlabel("乘客等级")
plt.ylabel("人数")

plt.show()