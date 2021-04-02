import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC, LinearSVC

df_train = pd.read_csv("titanic/train.csv")

######################################
# 전처리
# 1. 상관관계가 낮은 열을 삭제
df_train = df_train.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin"], axis=1)

# 2. 비어있는 칸(NaN) 채우기
# 아래 함수를 실행해보면 Age에 빈칸이 177 Embarked에 2개 있음
# print(df_train.isnull().sum())
df_train["Age"] = df_train["Age"].fillna(df_train["Age"].mean())

# Embarked 는 가장 많은 S로 채웠다.
df_train["Embarked"] = df_train["Embarked"].fillna("S")

# 3. 문자 데이터를 숫자로 변환하기
df_train["Sex"] = df_train["Sex"].map({"male": 0, "female": 1})
df_train["Embarked"] = df_train["Embarked"].map({"Q": 0, "C": 1, "S": 2})

######################################
# 학습하기
# 1. 분류기 생성. 여기서는 decision tree
#classifire = DecisionTreeClassifier()
classifire = RandomForestClassifier()
#classifire = LinearSVC()

# 2. 특징데이터와 정답데이터 분리
ground_truth = df_train["Survived"]
train_data = df_train.drop("Survived", axis=1)

# 3. 학습
classifire.fit(train_data, ground_truth)

# 4. 학습 결과 확인
print("Train Accuracy: ", round(classifire.score(train_data, ground_truth), 2))

######################################
# 테스트 셋에 대한 결과 생성

df_test = pd.read_csv("titanic/test.csv")

# 1. 학습 데이터와 똑같은 형태로 만들어준다.
# 결과물 제출시 passengerId는 필요하므로 따로 빼두었다.
pId = df_test["PassengerId"]
df_test = df_test.drop(["Name", "PassengerId", "Ticket", "Fare", "Cabin"], axis=1)
df_test["Age"] = df_test["Age"].fillna(df_test["Age"].mean())
df_test["Embarked"] = df_test["Embarked"].fillna("S")
df_test["Sex"] = df_test["Sex"].map({"male": 0, "female": 1})
df_test["Embarked"] = df_test["Embarked"].map({"Q": 0, "C": 1, "S": 2})

# 2. 분류기에 넣고 돌린다.
test_result = classifire.predict(df_test)

# 3. 결과물을 만든다.
submit = pd.DataFrame({"PassengerId": pId, "Survived": test_result})
#submit.to_csv("titanic/submit.csv", index=False)


######################################
# 테스트 셋 정답 파일과 비교.
# 캐글 결과가 약간의 차이가 있음.
test_gt = pd.read_csv("titanic/groundtruth.csv")
base = pd.read_csv("titanic/gender_submission.csv")

hit = 0
miss = 0

for i in range(len(test_result)):
    if base["Survived"][i] == test_gt["Survived"][i]:
        hit += 1
    else:
        miss += 1

print(hit, miss, round(hit/(hit+miss), 2))