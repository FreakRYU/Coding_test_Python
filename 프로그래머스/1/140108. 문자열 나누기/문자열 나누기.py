def solution(s):
    answer = 0
    
    while s:       
        x = s[0]
        count_x, count_not_x = 1, 0
        idx = 1
        length = len(s)
        
        while count_x != count_not_x and idx < length:
            if s[idx] == x:
                count_x += 1
            else:
                count_not_x += 1
            idx += 1
            
        s = s[idx:length]
        answer += 1
                    
    return answer