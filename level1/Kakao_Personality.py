def solution(survey, choices):
    check = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}


    for i in range(len(survey)):
        if choices[i] == 1:
            check[survey[i][0]] += 3
        elif choices[i] == 2:
            check[survey[i][0]] += 2
        elif choices[i] == 3:
            check[survey[i][0]] += 1
        elif choices[i] == 5:
            check[survey[i][1]] += 1
        elif choices[i] == 6:
            check[survey[i][1]] += 2
        elif choices[i] == 7:
            check[survey[i][1]] += 3


    result = ''

    for i in range(0, len(check.items()), 2):
        if list(check.values())[i] > list(check.values())[i+1]:
            result += list(check.keys())[i]
        elif list(check.values())[i] < list(check.values())[i+1]:
            result += list(check.keys())[i+1]
        else:
            a = sorted(list(check.keys())[i] + list(check.keys())[i+1])
            result += a[0]

    return result