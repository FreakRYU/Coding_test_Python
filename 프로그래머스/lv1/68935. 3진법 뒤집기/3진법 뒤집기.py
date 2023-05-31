def solution(n):
    # n을 3진법으로 변환
    base_3 = ''
    while n > 0:
        base_3 += str(n % 3)
        n //= 3
    
    # 3진법으로 변환된 수를 앞뒤로 뒤집기
    reversed_base_3 = base_3[::-1]
    
    # 뒤집힌 3진법을 10진법으로 변환하기
    decimal = 0
    for i in range(len(reversed_base_3)):
        decimal += int(reversed_base_3[i]) * (3 ** i)
    
    return decimal