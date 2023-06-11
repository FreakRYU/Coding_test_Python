def solution(k, score):
    stack = []
    answer = []
    
    for i in score:
        stack.append(i)
        stack.sort()
        stack = stack[-k:]
        answer.append(stack[0])
        
    return answer