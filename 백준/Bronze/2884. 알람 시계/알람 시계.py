import sys

a, b = map(int, sys.stdin.readline().strip().split())

if a == 0 and b < 45:
    a, b = 23, b + 15
    print(a, b)
    
else:
    a, b = (60 * a + b - 45) // 60, (60 * a + b - 45) % 60
    print(a, b)
    