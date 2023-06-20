def solution(k, m, score):
    l = len(score)
    score.sort(reverse = True)
    sum = 0
    
    for i in range(l//m):
        sum += score[(i+1)*m - 1]
        
    answer = sum * m
    return answer