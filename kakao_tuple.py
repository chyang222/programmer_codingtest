from collections import Counter

def solution(s):
    s = s.replace("{", "").replace("}", "")

    s = s.split(",")

    def ab(n):
        return int(n)

    s = list(map(ab, s))

    count_dict = Counter(s).most_common()
    answer = [item[0] for item in count_dict]

    return answer