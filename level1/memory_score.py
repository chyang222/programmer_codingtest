def solution(name, yearning, photo):
    answer = []
    di = {na:va for na, va in zip(name, yearning)}
    
    for i in photo:
        a = 0
        for j in i:
            if j in di.keys():
                a += di[j]
    
        answer.append(a)
    
    return answer

