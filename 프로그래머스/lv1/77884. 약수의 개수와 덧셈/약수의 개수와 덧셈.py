def solution(left, right):
    num = sum([-i if (i**(0.5))%1 == 0 else i 
               for i in range(left, right + 1)])
        
    return num 