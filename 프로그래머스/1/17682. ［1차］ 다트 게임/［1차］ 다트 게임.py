def solution(dartResult):
    dic = {
        'S' : lambda lst: lst[-1] ** 1,
        'D' : lambda lst: lst[-1] ** 2,
        'T' : lambda lst: lst[-1] ** 3,
        '*' : None, 
        '#' : lambda lst: -lst[-1]
    }
    
    answer = 0
    length = len(dartResult)
    num_list = []
    
    for i in range(0, length):
        if dartResult[i] not in dic:
            if num_list and num_list[-1] == 1 and dartResult[i] == '0':
                num_list[-1] = 10
            else:
                num_list.append(int(dartResult[i]))
        else:
            if dartResult[i] == '*':
                if len(num_list) == 1:
                    num_list[-1] = num_list[-1] * 2
                else:
                    num_list[-1], num_list[-2] = num_list[-1] * 2, num_list[-2] * 2
            else:
                num_list[-1] = dic[dartResult[i]](num_list)
        
    return sum(num_list)