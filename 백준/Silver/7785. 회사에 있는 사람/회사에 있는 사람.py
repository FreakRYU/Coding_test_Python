import sys

n = int(sys.stdin.readline())
dic = {}

for i in range(n):
    name, log = sys.stdin.readline().split()
    if name in dic and dic[name] == 'enter':
        del dic[name]
    else:    
        dic[name] = log

office = list(dic.keys())
office.sort(reverse=True)

for i in office:
    print(i)