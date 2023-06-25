import sys
a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

a, b = ((60*a+b+c)//60)%24, (60*a+b+c)%60
print(a, b)