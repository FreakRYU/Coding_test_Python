def solution(num, cnt=0):
    if cnt == 500:
        return -1
    
    elif num == 1:
        return cnt
    
    elif num % 2 == 0:
        cnt += 1
        return solution(num/2, cnt)
        
    else:
        cnt += 1
        return solution(num * 3 + 1, cnt)