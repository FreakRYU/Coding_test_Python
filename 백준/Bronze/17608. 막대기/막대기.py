import sys

n = int(input())
stack = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if not stack:
        stack.append(a)
    else:
        while stack and a >= stack[-1]: # 입력값이 top 원소보다 크면
            stack.pop()
        stack.append(a)

print(len(stack))