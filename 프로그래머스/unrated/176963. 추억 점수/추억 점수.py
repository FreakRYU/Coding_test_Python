def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning)) # 2개의 리스트로 딕셔너리 만들기 
    for i in range(len(photo)):     # 이중 리스트 photo에서 인덱스 순회
        cnt = 0                     # cnt 변수 도입
        for name in photo[i]:       # 인물이 담긴 사진에서 이름을 하나씩 색출
            if name in dic:         # 만약 꺼낸 이름이 dic에 있다면
                cnt += dic[name]    # dic에 저장된 그리움 점수를 cnt에 더함
        answer.append(cnt)          # 위 반복에서 그리움 점수를 합한 cnt를 answer에 추가함
    return answer