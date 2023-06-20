import sys

n = int(sys.stdin.readline())
num = map(int, sys.stdin.readline().split())
answer = [-1] * n
stack = []

# num에서 enumerate를 사용하여 인덱스와 입력된 숫자와 짝지어 준다.
for idx, number in enumerate(num):
    # stack의 top원소의 값이 stack으로 들어올 number보다 작다면
    while stack and stack[-1][1] < number:
        answer[stack[-1][0]] = number # answer에 값을 정의해준다.
        stack.pop()                   # 그리고 top 원소는 삭제
    stack.append((idx, number))

answer = ' '.join(map(str, answer))

print(answer)