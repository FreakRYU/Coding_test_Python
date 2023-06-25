import sys
n = int(sys.stdin.readline())

if n % 400 == 0:
    print(1) 
else:
    if n % 4 == 0 and n % 100:
        print(1) 
    else:
        print(0) 