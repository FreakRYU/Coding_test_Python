def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    answer = 0
    speak_stack = []
    
    for item in babbling:
        # 연속되는 발음이 문자열에 포함되면, 커트
        if "ayaaya" in item or "yeye" in item or "woowoo" in item or "mama" in item:
            continue
                
        # 연속되는 발음이 없다면, replace로 하나씩 제거
        for babb in speak:
            item = item.replace(babb, " ")
        
        # 임의로 넣은 공백 제거
        item = item.replace(" ", "")
        
        # 작업이 끝나고 빈문자열이면 카운트 +1
        if not item:
            answer += 1
        
    return answer