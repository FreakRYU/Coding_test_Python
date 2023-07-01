from collections import deque

n_1 = deque([1, 2, 3, 4, 5])
n_2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
n_3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
lst = [n_1, n_2, n_3]

def solution(answers):
    idx = 0
    answer = []
    pre_cnt = 0
    for n in lst:   
        idx += 1
        cnt = 0
        for i in answers:
            if i == n[0]:  
                cnt += 1
            n.append(n.popleft()) # 수포자 답안지를 원형큐로 구현
        if not answer:
            answer.append(idx)
        else:
            if cnt > pre_cnt:
                answer.clear()
                answer.append(idx)
            elif cnt == pre_cnt:
                answer.append(idx)
        pre_cnt = max(pre_cnt, cnt)
        
    answer.sort()
    return answer