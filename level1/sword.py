number = 10
limit = 3
power = 2

def solution(number, limit, power):
    val = []
    for n in range(1, number + 1):
        cnt = 0
        for i in range(1, int(n ** 0.5) + 1):
            if i**2 == n:
                cnt += 1
            elif n % i == 0:
                cnt += 2
        if cnt > limit:
            val.append(power)
        else:
            val.append(cnt)

    return sum(val)


solution(10, 3, 2)