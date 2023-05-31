def solution(array, commands):
    answer = []
    # 커멘드를 순회하면서 [i,j,k]를 탐색해줍니다.
    for ijk in commands:
        i, j, k = ijk
        n = array[i-1:j]
        n.sort()
        answer.append(n[k-1])
    return answer