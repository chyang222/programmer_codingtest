from collections import deque

def solution(first, second):
    first = deque(first)
    second = deque(second)
    count = 0
    total1 = sum(first)
    total2 = sum(second)
    limit = len(first) * 4

        
    while(total1 != total2):
        if total1 > total2:
            a = first.popleft()
            second.append(a)
            total1 -= a
            total2 += a
            count += 1
            limit -= 1

        elif total1 < total2:
            b = second.popleft()
            first.append(b)
            total1 += b
            total2 -= b
            count += 1
            limit -= 1

        if limit == 0:
            break

    if total1 != total2:
        return -1
    else:
        return count
