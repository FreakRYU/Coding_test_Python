def solution(strings, n):
    # 같은 문자열이 여럿일 경우를 대비해, 미리 사전순 정렬한다.
    strings.sort()
    # 자료.sort(key=함수) 를 이용해서 정렬의 기준을 정할 수 있다.
    strings.sort(key=lambda x:x[n])
    return strings

