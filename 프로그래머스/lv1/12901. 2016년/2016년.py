def solution(a, b):
    # 매달 일 수
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    
    # 1월 1일이 금요일이므로, 인덱스를 고려하여 목요일부터 시작
    name = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    # 7로 나누어 요일 연산
    index = (sum(day[0:a-1]) + b) % 7 
    
    answer = name[index]
    return answer