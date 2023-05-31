def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            return i
        elif budget == 0:
            return i+1
    return i+1
       