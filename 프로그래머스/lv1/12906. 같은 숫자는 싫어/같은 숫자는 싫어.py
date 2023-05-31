def solution(arr):
    arr2 = [arr[0]]
    for i in range(len(arr)):
        if arr[i] != arr2[-1]: # arr에서 순차적으로 탐색한 값이 arr2의 rear와 다르다면 
            arr2.append(arr[i]) # arr2에 arr의 top을 추가
    return arr2