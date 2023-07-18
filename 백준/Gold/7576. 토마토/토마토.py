from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
tomato = []
cnt_1 = 0
cnt_m1 = 0

for i in range(n):
    row = [int(x) for x in sys.stdin.readline().split()]
    for j in range(m):
        if row[j] == 1:
            graph[i][j] = 1
            tomato.append((i, j, 0))
            cnt_1 += 1
        if row[j] == -1:
            graph[i][j] = -1
            cnt_m1 += 1

def bfs(start):
    depth = 0
    q = deque(start)
    if not cnt_1:
        return -1
    if cnt_1 + cnt_m1 == m*n:
        return depth
    cnt = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        cur_i, cur_j, cur_d = q.popleft()
        for k in range(4):
            next_i = cur_i + dx[k]
            next_j = cur_j + dy[k]
            if 0 <= next_i < n and 0 <= next_j < m:
                if graph[next_i][next_j] == 0:
                    cnt += 1
                    q.append((next_i, next_j, cur_d+1))
                    graph[next_i][next_j] = 1
                    depth = max(depth, cur_d+1)

    cnt = cnt + cnt_1 + cnt_m1
    if cnt != m*n:
        return -1
    return depth

print(bfs(tomato))