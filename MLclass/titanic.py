import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df_train = pd.read_csv("titanic/train.csv")
#print(df_train.head())

#print(df_train.info())

# 생존자 수 확인
print(df_train["Survived"].value_counts())

# 생존 그룹과 그렇지 않은 그룹으로 나눈다.
survive = df_train.loc[df_train["Survived"] == 1].copy()
dead = df_train.loc[df_train["Survived"] == 0].copy()

print(survive["Pclass"].value_counts(sort=False))
print(dead["Pclass"].value_counts(sort=False))

df_train["Pclass"] = df_train["Pclass"]\
    .replace(1, "1st")\
    .replace(2, "Business")\
    .replace(3, "Economy")
df_train["Survived"] = df_train["Survived"]\
    .replace(1, "Alive")\
    .replace(0, "Dead")

seaborn.set_style(style="darkgrid")
seaborn.countplot(data=df_train, x="Pclass", hue="Survived")
plt.show()

