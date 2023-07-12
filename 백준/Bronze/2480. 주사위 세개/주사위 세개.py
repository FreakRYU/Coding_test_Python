import sys

a, b, c = map(int, sys.stdin.readline().split())

cnt = 0
n = 0

if a == b and b == c:  # 주사위의 숫자가 모두 같은 경우
    cnt = 3
    n = a
elif a == b or b == c or a == c:  # 두 개의 주사위 숫자가 같은 경우
    cnt = 2
    if a == b:
        n = a
    elif b == c:
        n = b
    else:
        n = a
else:  # 모든 주사위 숫자가 다른 경우
    n = max((a, b, c))

if cnt == 3:
    print(10000 + n * 1000)
elif cnt == 2:
    print(1000 + n * 100)
else:
    print(100 * n)