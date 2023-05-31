def solution(arr, divisor): 
    result = sorted(list(filter(lambda element: element % divisor == 0, arr)))
    if result == []:
        return [-1]
    return result

