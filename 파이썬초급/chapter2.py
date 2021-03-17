# 교재: 문제해결을 위한 소프트웨어 코딩 프로젝트 실습
#       김유두, 김종민 (한국폴리텍대학)
# 이 파일은 위 교재의 C 코드를 Python으로 코딩한 문서임
# 원 코드를 가급적 그대로 포팅함
# 코드 작성자: 강현우 (한국폴리텍대학)
'''
# [2-1] 화면에 단순 인사말 출력하기
print("안녕하세요")

# [2-2] 변수의 데이터 출력
bloodType = 'A'
height = 185
print("제 혈액형은 {0}형 이고, 키는 {1}cm 입니다.".format(bloodType, height))

# [2-3] 변수의 데이터 출력
math = 90
english = 85
programming = 100
print('수학\t\t영어\t\t프로그래밍')
print('{0}\t\t{1}\t\t{2}'.format(math, english, programming))

# [2-4] 새롭게 파일 내용 작성하기
fp = open('output.txt', 'w')
fp.write('제 이름은 홍길동이고, 나이는 20살 입니다.\n')
fp.close()

# [2-5] 기존 파일 내용에 추가로 작성하기
fp = open('output.txt', 'a')
fp.write('제 이름은 홍길동이고, 나이는 20살입니다.\n')
fp.close()

# [2-6] csv 파일 출력
fp = open('output.csv', 'w')
fp.write('name,Math,English,Programming\n')
fp.write('Hong,{0},{1},{2}\n'.format(90, 100, 70))
fp.write('Kim,{0},{1},{2}\n'.format(50, 90, 50))
fp.write('Poly,{0},{1},{2}\n'.format(60, 100, 90))
fp.write('Park,{0},{1},{2}\n'.format(100, 80, 70))
fp.close()

# [2-7] scanf 기본 동작 이해
input1, input2 = input().split()
print("반환 값: {0}, {1}\n".format(input1, input2))

# [2-8] scanf로 숫자 입력 받기
age = input()
print('나이: {0}'.format(age))

# [2-9] scanf로 숫자 입력 받기
height = input()
print("키: {0}".format(height))


# [2-10] 여러 숫자 한 번에 입력 받기
linuxScore, javaScore, cScore = input().split()
print('Linux: {0}'.format(linuxScore))
print('javaScore: {0}'.format(javaScore))
print('C: {0}'.format(cScore))

# [2-11] 문자 입력 받기
bloodType = input()
print('혈액형: {0}'.format(bloodType))

# [2-12] 문장 입력 받기
affilation = input()
print('소속: {0}'.format(affilation))

# [2-13] 문자와 숫자 혼합 입력 받기
digit1, operation, digit2 = input().split()
print('첫 번째 숫자: {0}'.format(digit1))
print('수식: {0}'.format(operation))
print('두 번째 숫자: {0}'.format(digit2))

# [2-14] FILE 입력 동작 확인
# [2-15] FILE 입력 동작 확인
fp = open('input.txt', 'r')
inputData = fp.readline()
print('입력 값: {0}'.format(inputData))
fp.close()

# [2-16] 정수 여러 개 파일에서 불러오기
fp = open('input.txt', 'r')
inputData = fp.readline().split()
print(inputData)
fp.close()

# [2-17] csv 데이터 파일에서 불러오기
fp = open('input.csv', 'r')
print('리눅스\t자바\tC언어')

data = fp.readlines()
for rows in data:
    rows = rows.rstrip('\n')
    cols = rows.split(',')
    for col in cols:
        if col != '\n':
            print(col, '\t', end=' ')
    print()

fp.close()
'''

salmonLength = [0, 0, 7, 17, 16, 11,
                0, 12, 0, 21, 0,
                20, 5, 3, 0, 9,
                5, 10, 1, 0, 10,
                3, 0, 9, 7, 3, 2]

bassLength = [0, 0, 0, 4, 5, 0,
                1, 8, 0, 5, 0,
                3, 6, 8, 0, 9,
                16, 18, 22, 0, 24,
                8, 0, 7, 6, 0, 0]

fp = open('salmon_bass_data.csv', 'w')
fp.write('Class,Length\n')

for i in range(27):
    for length in range(salmonLength[i]):
        fp.write('Salmon,{0}\n'.format(i))

for i in range(27):
    for length in range(bassLength[i]):
        fp.write('Bass,{0}\n'.format(i))

fp.close()