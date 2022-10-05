'''
for i in range(0,3,1):
    print("%d 안녕하세요? for문을 공부 중입니다. ^^" % i)
'''

'''
i, hap=0, 0

for i in range(1,11,1):
    hap = hap+i
print("1에서 10까지의 합: %d" %hap)
'''
'''
i, hap = 0, 0
num = 0

num = int(input("값 입려:"))

for i in range(1,num+1,1):
    hap = hap+i

print("1부터 %d까지의 합: %d"%(num, hap))
'''

'''
i, hap=0, 0

for i in range(100,201,2):
    hap = hap+i

print("100에서 200까지 2의 배수 합 : %d" %hap)
'''

'''
i, hap=0, 0

while i < 101:
    hap = hap + i
    i += 2

print("0에서 100까지의 짝수의 합 : %d" %hap)
'''
'''
mid = int(input("중간고사 점수를 입력하세요:"))
final = int(input("기말고사 점수를 입력하세요:"))
exam = int(input("과제점수를 입력하세요:"))
ab = int(input("결석 횟수를 입력하세요:"))

at = 20
if ab >= 2:
    at -= 5

if ab >= 5:
    print("F")

score = mid + final + exam + at

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
'''

''''
# 실습
# 1 ~ 100 사이 3의 배수 합과 원소 추출하기
cnt = 1
sum = 0
data = []

while cnt <= 100:
    cnt += 1
    if cnt % 3 == 0:
        sum += cnt
        data.append(cnt)
print("1 부터 100 까지 3의 배수 합 = %d" %sum)
print('data = ', data)
'''

'''
# 숫자 맞추기 게임
import random

print(">>숫자 맞추기 게임<< ")
com = random.randint(1, 10) # 1~10 사이 난수 발생

while True:
    my = int(input("예상 숫자를 입력하세요:")) # 숫자 입력
    if my == com: 
        print("~~ 성공 ~~")
    elif my > com:
        print("더 작은 수")
    elif my < com:
        print("더 큰 수")
'''

'''
su = []
sum = 0
for i in range(1,101):
    if i % 3 == 0 and i % 2 != 0:
        su.append(i)
        sum += i
print("수열 = ", su)
print("누적 합 =", sum)
'''







