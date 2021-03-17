# 교재: 문제해결을 위한 소프트웨어 코딩 프로젝트 실습
#       김유두, 김종민 (한국폴리텍대학)
# 이 파일은 위 교재의 C 코드를 Python으로 코딩한 문서임
# 원 코드를 가급적 그대로 포팅함
# 코드 작성자: 강현우 (한국폴리텍대학)

# [3-1] 간단한 버스 요금 경로 우대 처리 프로그램 만들기
age = 68
fee = 2000

if age >= 65:
    fee = 0

print('나이: {0}'.format(age))
print('요금: {0}'.format(fee))

# [3-2] 버스 요금 경로우대 처리 프로그램 만들기
age = int(input())
fee = 2000

if age >= 65:
    fee = 0

print('나이: {0}'.format(age))
print('요금: {0}'.format(fee))

# [3-3] 홀수 판단 프로그램 만들기
num = int(input('정수 입력: '))

if (num % 2) == 1:
    print('홀수')
else:
    print('짝수')

# [3-4] 오피스 자격증 합격 여부 프로그램 만들기
excel, powpoint, word = input('엑셀, 파워포인트, 워드: ').split()

sum = int(excel) + int(powpoint) + int(word)
avg = sum / 3

print('합계: {0}'.format(sum))
print('평균: {0}'.format(avg))

if (avg >= 60):
    print('합격')
else:
    print('불합격')

# [3-5] 위 프로그램에 합격 기준이 추가되었다.
excel, powpoint, word = input('엑셀, 파워포인트, 워드: ').split()

excel = int(excel)
powpoint = int(powpoint)
word = int(word)

sum = excel + powpoint + word
avg = sum / 3

print('합계: {0}'.format(sum))
print('평균: {0}'.format(avg))

if (avg >= 60) & (excel >= 40 & powpoint >= 40 & word >= 40):
    print('합격')
else:
    print('불합격')

# [3-6] 입력 점수에 따른 등급 출력
# 학생 점수 입력
score = int(input())
grade = 'F' # 초기값은 F로 설정

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'

print('학생 점수: {0}, 등급: {1}'.format(score, grade))

# [3-7] 산술 계산기
num1, oper, num2 = input("수식을 입력하시오 (ex) 2 + 3 :").split()

# 숫자(int)로 변환
num1 = int(num1)
num2 = int(num2)

if oper == '+':
    print('{0} + {1} = {2}'.format(num1, num2, num1+num2))
elif oper == '-':
    print('{0} - {1} = {2}'.format(num1, num2, num1-num2))
elif oper == '*':
    print('{0} * {1} = {2}'.format(num1, num2, num1*num2))
elif oper == '/':
    print('{0} / {1} = {2}'.format(num1, num2, round(num1/num2, 3)))
else:
    print('잘못된 입력입니다.')

# [3-8] 자연수 1~10 까지의 합을 구하는 프로그램
i = 1
sum = 0

while i <= 10:
    sum = sum + i
    i = i + 1

print('합계 = {0}'.format(sum))

# [3-9] 두 수의 범위의 합을 구하는 프로그램
sum = 0
start, end = input("2개의 정수를 입력하시오: ").split()

# 정수로 casting
start = int(start)
end = int(end)

while start <= end:
    sum = sum + start
    if start < end:
        print(start, '+ ', end="")
    else:
        print(start, '= ', end="")
    start = start + 1

print(sum)

# [3-12] 구구단 2단 출력 프로그램
print('\t2단')
for i in range(1, 10):
    print("2 * {0} = {1}".format(i, 2*i))

# [3-13] for문으로 정수 1~100 중 3의 배수 구하기
sum = 0

for i in range (1, 100):
    if i % 3 == 0:
        sum = sum + i
        print(i, end=" ")

print('\n1~100의 정수 중 3의 배수의 합 = {0}'.format(sum))