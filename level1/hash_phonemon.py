def solution(nums):
    limit = len(nums)/2
    re = [nums[0]]

    for i in nums:
        if i not in re and len(re) < limit:
            re.append(i)

    answer = len(re)
    
    return answer