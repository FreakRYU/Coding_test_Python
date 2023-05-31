def solution(absolutes, signs):
    return sum([(signs[i] and 1 or -1) * absolutes[i] 
                for i in range(len(absolutes))])