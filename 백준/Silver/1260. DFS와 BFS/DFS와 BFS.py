import sys 
from collections import deque

point, edge, start = map(int, sys.stdin.readline().split())

dic = {}

# 인접리스트로 저장
for _ in range(edge): 
    a, b = sys.stdin.readline().split()
    # 예외처리
    if not a or not b:
        continue

    else:
        a, b = int(a), int(b)
        if a != b:
            if a not in dic:
                dic[a] = [b]
            else:
                dic[a].append(b)

            if b not in dic:
                dic[b] = [a]
            else:
                dic[b].append(a)

# 정점 번호가 작은 것을 먼저 방문하기 위한 정렬
for key in dic:
    dic[key] = sorted(dic[key])

# DFS 수행
visit = []
def dfs(start_v):
    visit.append(start_v)
    if start not in dic:
        return
    
    for v in dic[start_v]:
        if v not in visit:
            dfs(v)
dfs(start)
output = ' '.join(map(str, visit))
    
# BFS 수행 
def bfs(start_v):
    q = deque()
    q.append(start_v)
    visited = [start_v]
    if start not in dic:
        return start_v

    while q:
        cur_v = q.popleft()
        for v in dic[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)

    output = ' '.join(map(str, visited))
    return output

# 출력
print(output)
print(bfs(start))