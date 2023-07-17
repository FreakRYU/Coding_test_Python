import sys
from collections import deque

n = int(sys.stdin.readline())
dic = {}

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] = dic.get(a, [])+[b]
    dic[b] = dic.get(b, [])+[a]

def dfs(start=1):
    q = deque()
    q.append(start)
    visited = {start:True}
    output = []

    while q:
        cur_v = q.popleft()
        for v in dic[cur_v]:
            if v not in visited:
                q.append(v)
                visited[v] = cur_v

    for i in range(2, n+1):
        output.append(visited[i])
    
    output = '\n'.join(map(str, output))
    return output

print(dfs(1))