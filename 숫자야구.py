from random import *
from numpy import *

# 숫자 정하기
abc = random.choice(range(0,10), 3, replace=False)
d = 0
ball = 0
strike = 0
out = 0

a = abc[0]
b = abc[1]
c = abc[2]

# 게임 시작하기

while d <= 9:
    d += 1
    ㅁ = int(input("첫번째 숫자는?"))
    ㅠ = int(input("두번째 숫자는?"))
    ㅊ = int(input("세번째 숫자는?"))
    if a == ㅁ:
        strike += 1;
    elif b == ㅁ:
        ball += 1;
    elif c == ㅁ:
        ball += 1;
    else:
        out += 1;

    if a == ㅠ:
        ball += 1;
    elif b == ㅠ:
        strike += 1;
    elif c == ㅠ:
        ball += 1;
    else:
        out += 1;

    if a == ㅊ:
        strike += 1;
    elif b == ㅊ:
        ball += 1;
    elif c == ㅊ:
        strike += 1;
    else:
        out += 1;
    
    # 결과 알려주기

    print("{}스크라이크, {}볼, {}아웃".format(strike, ball, out))
    if strike == 3:
        print("승리~~!")
        input()
        exit()
    else:
        input()
    strike = 0;
    ball = 0;
    out = 0;

# 게임 결과 알려주기

if strike == 3:
    print("승리~~")
else:
    print("패배..")
    print(abc , "였어요")