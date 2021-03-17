import pandas as pd

#df = pd.read_csv('salmon_bass_data.csv')


# dictionary 생성 {key, value}
dic = {'name': '강현우'}
print(dic)

# key값을 인덱스처럼 사용이 가능
print(dic['name'])

# 새로운 값 할당 가능
dic['name'] = '김동규'
print(dic)

# 하나의 key 에 여러개의 value (list) 할당
nameList = ['강현우', '김동규', '김미경']
dic['name'] = nameList
print(dic)

# 새로운 key 값 추가
dic['id'] = [0, 1]
print(dic)

# dictionary[key] 가 하나의 list이므로
# 리스트 연산이 가능. 예) 리스트 값 추가 append
dic['id'].append(2)
print(dic)

df = pd.DataFrame(dic)
print(df)

# DataFrame 에 열(col) 추가. key를 추가하듯이..
# 하나의 값으로 열을 초기화
df['국어'] = 0
print(df)

# 실제 값을 할당할 수도 있음
df['국어'] = [100, 100, 100]
print(df)

# 점수는 랜덤으로..
import random as r
def score():
    return r.randint(0, 100)

df['국어'] = [score(),score(), score()]
print(df)

# 행을 접근 할 경우에는 loc[index]
# 기존의 행을 바꾸기
df.loc[0] = ['김대현', '2021-1', score()]
print(df)

# 새로 행 추가하기
df.loc[3] = ['김재웅', '2021-5', score()]
df.loc[4] = 0
print(df.shape)

# shape 이용하여 행 추가 shape = (행, 열)
df.loc[df.shape[0]] = ['김창우', '2021-7', score()]
print(df)

# loc [행, 열] 로 접근
# df.loc[1]['id'] = '2021-2'    # 이렇게 쓰지 마라고 함
df.loc[1, 'id'] = '2021-2'
df.loc[2, 'id'] = '2021-3'
df.loc[4] = ['김지원', '2021-6', score()]
print(df)

# 한번에 22번까지 추가
# shape[0] 대신 len을 사용할 수도 있다.
for i in range(len(df), 22):
    df.loc[i] = ['name-{0}'.format(i),
                 '2021-{0}'.format(i+2), score()]

# 그러나 이름은... 법칙이 없다.
# 개별로 고칠수 밖에
df.loc[6, 'name'] = '박동주'
df.loc[7, 'name'] = '박종균'
df.loc[8, 'name'] = '서지완'
df.loc[9, 'name'] = '손이나'
df.loc[10, 'name'] = '신나리'

print(df)

# 새로운 행을 가운데에 추가 하고자 할 경우
# 여기서는 3번 인덱스에 추가 하고자 함
idx = 3
#
# 인덱스를 기준으로 2개로 분할
# copy()가 없으면 어떻게 될까?!
temp1 = df[df.index < idx].copy()
temp2 = df[df.index >= idx]

#temp1 뒤에 새로운 행 추가
temp1.loc[len(temp1)] = ['김장원', '2021-4', score()]

# 자른거 2개를 합친다.
# ignore_index 옵션이 없으면 어떻게 되는가?
df = temp1.append(temp2, ignore_index=True)
print(df)

df.loc[12, 'name'] = '안정현'
df.loc[13, 'name'] = '이병훈'
df.loc[14, 'name'] = '이승휘'
df.loc[15, 'name'] = '이연우'
df.loc[16, 'name'] = '전진아'
df.loc[17, 'name'] = '조경민'
df.loc[18, 'name'] = '차혜인'
df.loc[19, 'name'] = '추승오'
df.loc[20, 'name'] = '한창협'
df.loc[21, 'name'] = '허윤석'
df = df.drop(22)

df['영어'] = 0
df['수학'] = 0

for i in range(len(df)):
    df.loc[i, '영어'] = score()
    df.loc[i, '수학'] = score()
print(df)

df.to_csv("ai_score_data.csv")