import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
stack = []
answer = []
cnt = 0

# 입력받은 정수와 1부터 시작하는 인덱스를 짝지어 준다.
for index, num in enumerate(data, start = 1): 
    while stack and num > stack[-1][0]:
        stack.pop()

    if not stack: # stack에 아무것도 없어야 실행됨
        answer.append(0)
        stack.append((num, index))
    
    else: # stack에 원소가 있다면
        answer.append(stack[-1][1])
        stack.append((num, index))

print(' '.join(map(str, answer)))