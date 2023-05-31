def solution(price, money, count):
    result = money - price * sum(range(1, count+1)) 
    if result < 0:
        return -result 
    return 0
