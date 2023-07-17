from collections import deque
import sys

n = int(sys.stdin.readline())
start, end = map(int,sys.stdin.readline().split())
edge = int(sys.stdin.readline())
dic = {}

for i in range(edge):
	a, b = map(int, sys.stdin.readline().split())
	dic[a] = dic.get(a, []) + [b]
	dic[b] = dic.get(b, []) + [a]
	
def bfs(start, end):
	q = deque()
	q.append((start, 0))
	visited = {start: True}
	
	while q:
		cur_v, cur_cnt = q.popleft()
		for v in dic[cur_v]:
			if v not in visited:
				if v == end:
					return cur_cnt+1
				else:
					q.append((v, cur_cnt+1))
					visited[v] = True
					
	return -1

print(bfs(start, end))