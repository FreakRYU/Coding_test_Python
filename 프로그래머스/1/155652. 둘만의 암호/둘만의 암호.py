def solution(s, skip, index):
    alpa = 'abcdefghijklmnopqrstuvwxyz'
    # acefghijklmnoprstuvxyz
    answer = ''
    
    for w in skip:
        alpa = alpa.replace(w, '')
    
    length = len(alpa)
    
    for i in s:
        idx = alpa.index(i) + index
        if idx > (length - 1):
            idx = (idx+1) % length - 1
        answer += alpa[idx]
    
    return answer