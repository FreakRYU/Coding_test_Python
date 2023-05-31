def solution(n):
    for i in range(1, n+1):
        if n/i == i:
            return (i+1)**2
        else:
            continue
    return -1
        
        