import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.reshape.reshape import stack

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

#看看各性别的获救情况
fig = plt.figure()
# 设定图表颜色alpha参数
fig.set(alpha=0.2)

#男性数量
Survived_m = titanic.survived[titanic.sex == 'male'].value_counts()
#女性数量
Survived_f = titanic.survived[titanic.sex == 'female'].value_counts()

df = pd.DataFrame({u'男性': Survived_m, u'女性': Survived_f})
df.plot(kind='bar', stacked=True)
plt.title(u'按性别看获救情况')
plt.xlabel(u'性别')
plt.ylabel(u'人数')
plt.show()