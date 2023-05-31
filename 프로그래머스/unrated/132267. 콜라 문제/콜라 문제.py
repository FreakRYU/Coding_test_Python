def solution(a, b, n):
    # a: b개의 콜라를 받기 위해 가져다 주는 빈병 개수, b: 돌려받는 콜라 개수, n: 가지고 있는 빈병 개수
    cnt = 0
    while n >= a:
        cnt += (n//a) * b
        n = (n//a) * b + n%a
    return cnt