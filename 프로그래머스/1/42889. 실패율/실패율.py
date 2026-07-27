def solution(N, stages):
    dic = {}
    
    # 1부터 N 까지 스테이지를 순회
    for i in range(1, N+1):
        # 실패율 = (배열에서 해당 스테이지 번호의 개수) / (그 번호보다 크거나 같은 수의 개수)
        not_clear = stages.count(i)
        reach = sum([1 for x in stages if x >= i])
        failure = 0
        if reach != 0:
            failure = not_clear / reach
        dic[i] = failure
    
    answer = sorted(dic, key=lambda stage: dic[stage], reverse=True)
    return answer