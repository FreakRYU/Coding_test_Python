def solution(s, n):
    answer = ''
    for c in s:
        # 알파벳인 경우에만 밀기 연산 수행
        if c.isalpha():
            # 대문자 알파벳의 경우
            if c.isupper():
                answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
            # 소문자 알파벳의 경우
            else:
                answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        # 알파벳이 아닌 경우는 그대로 추가
        else:
            answer += c
    return answer