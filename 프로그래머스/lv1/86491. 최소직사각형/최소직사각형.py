def solution(sizes):
    length = 0
    height = 0
    for card in sizes:
        if max(card) > length:
            length = max(card)
            
        if min(card) > height:
            height = min(card)
        
    return length * height