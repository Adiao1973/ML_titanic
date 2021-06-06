import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

fig = plt.figure(figsize=(15, 10))
# 设置图像透明度，无所谓
fig.set(alpha=0.65)
plt.title(u"根据舱等级和性别的获取情况")

ax1 = fig.add_subplot(141)
titanic.survived[titanic.sex == 'female'][
    titanic.pclass != '3rd'].value_counts().plot(kind='bar',
                                                 label="female highclass",
                                                 color='#FA2479')
ax1.set_xticklabels([u'获救', u'未获救'], rotation=0)
ax1.legend([u'女性/高级舱'], loc='best')

ax2 = fig.add_subplot(142, sharey=ax1)
titanic.survived[titanic.sex == 'female'][
    titanic.pclass == '3rd'].value_counts().plot(kind='bar',
                                                 label="female lowclass",
                                                 color='pink')
ax2.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u'女性/低级舱'], loc='best')

ax3 = fig.add_subplot(143, sharey=ax1)
titanic.survived[titanic.sex == 'male'][
    titanic.pclass != '3rd'].value_counts().plot(kind='bar',
                                                 label="male highclass",
                                                 color='steelblue')
ax3.set_xticklabels([u'未获救', u'获救'], rotation=0)
plt.legend([u'男性/高级舱'], loc='best')

ax4 = fig.add_subplot(144, sharey=ax1)
titanic.survived[titanic.sex == 'male'][
    titanic.pclass == '3rd'].value_counts().plot(kind='bar',
                                                 label='male lowclass',
                                                 color='lightblue')
ax4.set_xticklabels([u'未获救', u'获救'], rotation=0)
plt.legend([u'男性/低级舱'], loc='best')

plt.show()
