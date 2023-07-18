import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
dic = {}
for i in num:
    dic[i] = dic.get(i, 0) + 1
answer = [-1]*n
stack = []

for idx, value in enumerate(num):
    while stack and dic[value] > dic[stack[-1][0]]:
        answer[stack[-1][1]] = value
        stack.pop()
    stack.append((value, idx))

answer = ' '.join(map(str, answer))
print(answer)