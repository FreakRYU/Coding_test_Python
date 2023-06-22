import sys

n  = int(sys.stdin.readline())
dic = {}
max_score = 1

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # x, y의 위치벡터를 정규화한다.
    x, y = x and x/abs(x), y/abs(x) if x else y/abs(y)
    
    if (x, y) in dic:
        dic[(x, y)] = dic[(x, y)] + 1
        if dic[(x, y)] > max_score:
            max_score = dic[(x, y)]
    else:
        dic[(x, y)] = 1
    
print(max_score)