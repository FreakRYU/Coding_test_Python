import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
memo = set(data)

for i in data:
    i = ''.join(reversed(i))
    if i in memo:
        s = len(i)
        mid_letter = i[s//2]
        print(f"{s} {mid_letter}")
        break