def solution(absolutes, signs):
    a = []
    for i in range(len(signs)):
        if signs[i] == False:
            a.append(-absolutes[i])
        else:
            a.append(absolutes[i])
        
    answer = 0
    for i in a:
        answer += i
    return answer