import sys 
from collections import deque

computer = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

dic = {}

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)

    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)

def bfs(start_v = 1):
    q = deque()
    q.append(start_v)
    visited = [1]
    if 1 not in dic:
        return 0
    
    while q:
        cur_v = q.popleft()
        for v in dic[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    
    return len(visited)-1

print(bfs())