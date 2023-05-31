def solution(n):
    for x in range(2, n+1):
         if (n-1) % x == 0:
                return x
   
