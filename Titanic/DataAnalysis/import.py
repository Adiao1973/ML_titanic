import pandas as pd
import os

titanic = pd.read_csv("Titanic\DataSet\\train\\titanic.csv")

print(titanic.head(5))
print(titanic.info())