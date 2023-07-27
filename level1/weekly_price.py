def solution(price, money, count):
    
    pri = [price * cnt for cnt in range(1, count+1)]
    
    a = sum(pri) - money
    
    if a > 0:
        return a
    else:
        return 0