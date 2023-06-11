# k번째 전 원소를 모두 뒤로 보내고(k-1번 시행) 
# q[0]를 answer에 추가하고 pop
import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
answer = []

q = deque()
for i in range(1, a+1):
    q.append(i)

while len(q):
    for _ in range(b-1):
        q.append(q[0])
        q.popleft()
    answer.append(str(q[0])) # answer에 추가되는 원소를 str로 변환
    q.popleft()

answer = ', '.join(answer)

# str과 int는 연산이 안되므로 answer의 원소를 str로 변환해야함.
print('<' + answer + '>')