import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai_score_data.csv")
'''
print(df.shape)
print(df.info())
print(df.describe())

# 모든 열의 평균
print(df.mean())

# 특정 열의 평균
print(df['Math'].mean())
print(df.Math.mean())

# 중간값 (중간값은 평균이 아님)
print(df['Korean'].median())
print(df.English.median())

# 최대/최소 값
print(df.Math.max())
print(df.Math.min())
print(df.English.max())
print(df.English.min())
print(df.Korean.max())
print(df.Korean.min())

# 표준 편차
print(df.Math.std())
print(df.Math.std())
print(df.English.std())

# 두 열 사이의 상관 계수. [ 가 2개임에 주의
print(df[['Math', 'Korean']].corr(), '\n')
print(df[['Math', 'English']].corr(),'\n')
print(df[['Korean', 'English']].corr(),'\n')

# 모든 열 사이의 상관 계수
print(df.corr())

# 차트 꾸미기
plt.title('Math Score')     # 제목
plt.xlabel('Score')         # x축 label
plt.xticks(range(0, df.Math.max(), 5))  #범위, step
plt.ylabel('Count')         # y축 label
plt.hist(df['Math'], bins=20)   # 히스트로그램 구간


canvas = plt.figure(figsize=(7.0, 7.0)) # 이미지 크기 조절
plt.grid()                              # 격자 표현
# color, marker 모양
plt.scatter(df['Math'], df['English'],color='red', marker='P')

# 점 하나 씩도 가능
plt.scatter(df.loc[0, 'Math'], df.loc[0, 'English'],
            color='red', marker='P')    # 플러스 모양
plt.scatter(df.loc[1, 'Math'], df.loc[1, 'English'],
            color='blue', marker='D')   # 다이아몬드
plt.scatter(df.loc[2, 'Math'], df.loc[2, 'English'],
            color='yellow', marker='h')   # 헥사곤
plt.scatter(df.loc[3, 'Math'], df.loc[3, 'English'],
            color='green', marker='x')   # x
plt.show()
'''

canvas = plt.figure(figsize=(7.0, 7.0))
plt.xlabel('Math Score')
plt.ylabel('English Score')
for i in range(len(df['Sex'])):
    if df['Sex'][i] == '남':
        plt.scatter(df['Math'][i], df['English'][i], color='blue')

    else:
        plt.scatter(df['Math'][i], df['English'][i], color='red')

plt.show()