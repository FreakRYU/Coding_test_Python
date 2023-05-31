def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total = numbers[i] + numbers[j]
            answer.append(total)
    answer = list(set(answer))
    answer.sort()
    return answer