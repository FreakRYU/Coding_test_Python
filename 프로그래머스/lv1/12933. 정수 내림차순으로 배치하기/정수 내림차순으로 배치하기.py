def solution(n):
    return int(''.join(str(num) for num in [int(i) for i in sorted(str(n), reverse=True)]))