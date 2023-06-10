import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]

stack = [] # stack에 튜플 형태로 저장
total = 0

# data에서 역순으로 꺼내어 전개
for i in reversed(range(n)): 
    cnt = 0 # 매 반복마다 cnt 값 초기화

    if not stack: # stack이 비어있다면 실행됨.
        stack.append((data[i], cnt))

    else:
        # 추가해야할 값이 top보다 크다면
        while stack and data[i] > stack[-1][0]: 
            # stack의 top 원소를 지우기 위해서, top이 가진 cnt값을 누적해야 함.
            cnt += (1 + stack[-1][1])
            stack.pop()
        stack.append((data[i], cnt))
        total += cnt

print(total)