def solution(s):
    # s를 공백도 포함하여 문자열을 리스트로 변환
    words = list(s)
    
    # 카운트 변수 
    cnt = 0
    
    # 생성된 word 리스트를 순회한다.
    for i in range(len(words)):
        
        # 문자열을 만나면 cnt +=1
        if words[i].isalpha():
            
            # 단어의 짝수번째 알파벳은 대문자로
            if cnt % 2 == 0: 
                words[i] = words[i].upper()
                
            # 단어의 홀수번째 알파벳은 소문자로    
            else: 
                words[i] = words[i].lower()
                
            cnt += 1
            
        # 공백을 만나면 cnt = 0 으로 초기화 한다   
        else:
            cnt = 0
            
    # "".join() 함수를 이용해서 리스트의 요소들을 문자열로 변환한다.        
    return "".join(words)