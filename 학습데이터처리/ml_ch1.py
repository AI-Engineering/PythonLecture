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
df.loc[3] = ['김재웅', '2021-4', score()]
df.loc[4] = 0

# shape 이용하여 행 추가 shape = (행, 열)
print(df.shape)
df.loc[df.shape[0]] = ['김창우', '2021-5', score()]
print(df)

# loc [행, 열] 로 접근
# df.loc[1]['id'] = '2021-2'    # 이렇게 쓰지 마라고 함
df.loc[1, 'id'] = '2021-2'
df.loc[2, 'id'] = '2021-3'
df.loc[4] = ['김지원', '2021-5', score()]
print(df)

# 한번에 22번까지 추가
for i in range(df.shape[0], 23):
    df.loc[i] = ['name-{0}'.format(i),
                 '2021-{0}'.format(i), score()]

# 그러나 이름은... 법칙이 없다.
df.loc[6, 'name'] = '박동주'
df.loc[7, 'name'] = '박종균'
df.loc[8, 'name'] = '서지완'
df.loc[9, 'name'] = '손이나'
df.loc[10, 'name'] = '신나리'


print(df)