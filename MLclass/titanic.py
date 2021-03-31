import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df_train = pd.read_csv("titanic/train.csv")

# 생존자 수 확인
print(df_train["Survived"].value_counts())


# count plot
def showCountPlot(feature):
    seaborn.countplot(data=df_train, x=feature, hue="Survived")
    plt.show()

# 데이터 전처리
# 필요없는 칼럼 삭제
df_train = df_train.drop("PassengerId", axis=1)
df_train = df_train.drop("Name", axis=1)
df_train = df_train.drop("Fare", axis=1)
df_train = df_train.drop("Cabin", axis=1)
df_train = df_train.drop("Ticket", axis=1)

df_train["Pclass"] = df_train["Pclass"]\
    .replace(1, "1st")\
    .replace(2, "Business")\
    .replace(3, "Economy")
df_train["Survived"] = df_train["Survived"]\
    .replace(1, "Alive")\
    .replace(0, "Dead")

# 나이를 그룹 별로
# 비어있는 값을 채움
df_train["Age"].fillna(df_train["Age"].mean(), inplace=True)

for i in range(len(df_train)):
    age = int(df_train.loc[i, "Age"] / 10)
    df_train.loc[i, "Age"] = age

df_train["Age"] = df_train["Age"].map({ 0:"Kids", 1:"Teen", 2:"20s",
                                 3:"30s", 4:"40s", 5:"50s", 6:"60s",
                                 7:"Old", 8:"Old"})


# 생존 그룹과 그렇지 않은 그룹으로 나눈다.
df_survive = df_train.loc[df_train["Survived"] == "Alive"]
df_dead = df_train.loc[df_train["Survived"] == "Dead"]

#print(df_survive["Pclass"].value_counts(sort=False))
#print(df_dead["Pclass"].value_counts(sort=False))

seaborn.set_style(style="darkgrid")

# 각 칼럼의 생존자 비율을 그리는 함수 (전체 생존자 비율)
def show_survive_rate(feature):
    # feature 열의 생존자 수를 카운트 한다.
    sur_info = df_survive[feature].value_counts(sort=False)
    print(sur_info)

    # 전체 생존자 수 대비 category 별 생존 비율
    category = sur_info.index
    plt.title("Survival Rate in Total ({0})".format(feature))
    plt.pie(sur_info, labels=category, autopct="%0.1f%%")
    plt.show()

# 각 칼럼의 인원수 대비 생존자 비율
def show_group_rate(feature):
    # Alive 와 dead 의 비율을 봐야 하므로 둘다 가져온다.
    sur_info = df_survive[feature].value_counts(sort=False)
    dead_info = df_dead[feature].value_counts(sort=False)
    print(sur_info)

    fig = plt.figure(figsize=(len(sur_info)*3, 3))

    plt.title("Survival rete of " + feature)

    for i, index in enumerate(sur_info.index):
        fig.add_subplot(1, len(sur_info), i+1)
        plt.pie([sur_info[index], dead_info[index]],
                labels=["Survived", "Dead"], autopct="%0.1f%%")
        plt.title("Survial rate of " + index)

    plt.show()

show_group_rate("Age")
