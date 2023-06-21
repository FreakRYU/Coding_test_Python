import sys

n = int(sys.stdin.readline())
dic = {}
stack = []
cnt = 0

# 터널로 들어가는 차(key)에 등수(0, 1, 2, 3, 4)를 value로 정의한다
for i in range(n):
    incar = sys.stdin.readline()
    dic[incar] = i

# 스택 사용, n개 만큼 다시 하번차를 입력받는다.
for j in range(n):
    outcar = sys.stdin.readline()
    # stack의 top 원소 상번등수가 뒷 하번차의 상번등수보다 높다면
    while stack and stack[-1][1] > dic[outcar]:
        stack.pop()
        cnt += 1
    stack.append((outcar, dic[outcar]))

print(cnt)