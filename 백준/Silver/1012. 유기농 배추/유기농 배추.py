from collections import deque
import sys

# (i, j)에서 BFS 수행, return은 없으며 탐색한 좌표는 True로 바꿔줌
def bfs(i, j, graph):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    while q:
        cur_r, cur_c = q.popleft()
        # 지정된 좌표의 상하좌우에 위치한 정점들을 정의
        for d in direction:
            next_r = cur_r + d[0]
            next_c = cur_c + d[1]
            # 우선 인접한 정점이 범위에 만족하는지 확인
            if 0 <= next_r <= row-1 and 0 <= next_c <= col-1:
                # 탐색할 곳이 배추를 심은 곳이고 방문하지 않았다면 수행됨
                if graph[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True

# 테스트 케이스 입력받기
tc = int(sys.stdin.readline())
output = []

for _ in range(tc):
    # 배추 위치 가로, 세로, 배추 개수 입력받기
    col, row, k = map(int, sys.stdin.readline().split())

    # 밭에 배추 심어주기
    graph = [[0]*col for _ in range(row)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    # 모든 좌표에 bfs 수행, 그리고 수행할 때마다 카운트함
    visited = [[False]*col for _ in range(row)]
    cnt = 0 
    for i in range(row):
        for j in range(col):
            # (i, j)가 bfs 수행이 가능한지 미리 판별
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j, graph)
                cnt += 1
    output.append(cnt)

for n in output:
    print(n)