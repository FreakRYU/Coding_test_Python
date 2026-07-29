def solution(lottos, win_nums):
    answer = []
    hit_max, hit_min = 0, 0
    
    for number in lottos:
        if number == 0:
            hit_max += 1
        else:
            if number in win_nums:
                hit_max += 1
                hit_min += 1
    
    if hit_max <= 1:
        answer.append(6)
    else:
        answer.append(7-hit_max)
    
    if hit_min <= 1:
        answer.append(6)
    else:
        answer.append(7-hit_min)
        
    return answer