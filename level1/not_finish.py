def solution(part, comple):
    hash_table = {}
    sumhash = 0
    
    for i in part:
        hash_table[hash(i)] = i
        sumhash += hash(i)
    
    for j in comple:
        sumhash -= hash(j)

    return hash_table[sumhash]