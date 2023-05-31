def solution(n, arr1, arr2):
    answer = []
    # 입력받은 배열에서 숫자 하나씩 꺼낸다
    for i in range(n):
        # 입력받은 숫자를 2진수로 나타내고 리스트로 변환한다.
        str1 = bin(arr1[i])[2:].zfill(n)
        str2 = bin(arr2[i])[2:].zfill(n)
        spare = ''
        for j in range(n):
            plus = int(str1[j])+int(str2[j]) and '#' or ' '
            spare += plus
        answer.append(spare)
    return answer
            