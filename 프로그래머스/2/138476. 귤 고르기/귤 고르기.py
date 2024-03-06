def solution(k, tangerines):
    dict = {}
    answer = 0
    for tangerine in tangerines:
        if tangerine not in dict:
            dict[tangerine] = 1
        else:
            dict[tangerine] += 1
    value = list(dict.values())
    value.sort(reverse=True)
    
    for val in value:
        k = k - val
        answer += 1
        if k <= 0:
            break
    
    return answer