from collections import deque
import sys

# deque 선언
q = deque()

n = int(sys.stdin.readline())
for i in range(n):
    q.append(i+1)

memo = []

while len(q) > 1:
    memo.append(q[0])
    q.popleft()
    q.append(q[0])
    q.popleft()

memo.append(q[0])

print(' '.join(map(str, memo)))
