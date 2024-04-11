def solution(gems):
    answer = [0, len(gems)]
    
    gems_set = set(gems)
    gems_length = len(gems_set)

    if gems_length == 1:
        return [1, 1]
    
    start, end, gems_count = 0, 1, 1
    gems_dict = {gems[start]: [0]}
    while end < len(gems):
        gem = gems[end]
        if gem in gems_dict:
            gems_dict[gem].pop(0)
            gems_dict[gem].append(end)
        else:
            gems_dict[gem] = [end]
            gems_count += 1
            
        if gems_count == gems_length:
            start = sorted(gems_dict.items(), key=lambda x:x[1])[0][1][0]
            
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            start, end, gems_count = start + 1, start + 1, 1
            if start > len(gems) - 1:
                return [answer[0] + 1, answer[1] + 1]
            gems_dict = {gems[start]: [start]}
            
        end += 1

    return [answer[0] + 1, answer[1] + 1]
