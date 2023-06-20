import sys

n = int(sys.stdin.readline())
a = sys.stdin.readline().strip()

for i in map(int, reversed(list(a))):
    print(n*i)

print(n*int(a))
