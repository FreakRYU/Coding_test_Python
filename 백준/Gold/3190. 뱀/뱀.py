import sys
from collections import deque

# 격자의 크기
n = int(sys.stdin.readline().strip()) 

# 사과의 좌표
apple = int(sys.stdin.readline().strip())

# 딕셔너리
apple_dic = {}
way_dic = {}

# 시간
cnt = 0

# 뱀이 격자에서 차지하고 있는 좌표 집합
q = deque()
q.append((1, 1))
snake_set = {(1, 1)}

# 방향전환
a, b = 0, 1
top = q[-1][0]+a, q[-1][1]+b

# 사과의 좌표를 apple_dic에 저장
for i in range(apple):
    x, y = map(int, sys.stdin.readline().split())
    apple_dic[(x, y)] = True
    
# 방향 전환을 way_dic에 저장
way = int(sys.stdin.readline())
for i in range(way):
    time, direction = sys.stdin.readline().split()
    way_dic[int(time)] = direction

# 뱀이 여전히 격자 안에 있고, 자신의 몸과 부딪히지 않는다면
while True:

    # 시간 카운트
    cnt += 1 

    # 뱀 머리의 다음 위치는 시간이 끝나고 방향변환을 한 후 적용
    nx, ny = q[-1][0] + a, q[-1][1] + b 

    # 뱀이 격자 범위를 벗어나거나 자신의 몸과 부딪혔을 때 게임 종료
    if not (1 <= nx <= n) or not (1 <= ny <= n) or (nx, ny) in snake_set:
        break

    # 뱀이 이동한 위치에 사과가 있다면
    if (nx, ny) in apple_dic:
        q.append((nx, ny))            # 머리 좌표 추가
        snake_set.add((nx, ny))       # 해시set에도 추가
        del apple_dic[(nx, ny)]       # 먹은 사과는 apple_dic에서 제거

    # 사과가 없다면    
    else:
        q.append((nx, ny))                  # 머리 좌표 추가
        snake_set.add((nx, ny))             # 해시set에도 추가
        snake_set.remove(q.popleft())       # 꼬리 좌표 삭제

    # 90도 선형변환
    if cnt in way_dic:
        if way_dic[cnt] == "L":     # 왼쪽 방향 변경
            a, b = -b, a
        elif way_dic[cnt] == "D":   # 오른쪽 방향 변경
            a, b = b, -a

print(cnt)