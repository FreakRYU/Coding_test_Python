import sys
string = sys.stdin.readline().rstrip()
s = sys.stdin.readline().rstrip()

stack = []

for i in string:
    stack.append(i)
    if len(stack) >= len(s) and ''.join(stack[-len(s):]) == s:
        del stack[-len(s):]

stack = ''.join(stack)

if stack:
    print(stack)

else:
    print('FRULA')