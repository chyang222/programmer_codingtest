def solution(array, com):
    answer = []
    
    for i in com:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    
    return answer