def solution(n, m):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcd_num = gcd(n, m)
    lcm_num = n * m // gcd_num
    
    return [gcd_num, lcm_num]