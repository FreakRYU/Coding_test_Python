import sys

n = int(sys.stdin.readline())

data = [int(sys.stdin.readline().strip()) for i in range(n)]
stack = []

for num in data:
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))