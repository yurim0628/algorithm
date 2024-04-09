from itertools import product

def solution(user_ids, banned_ids):
    answer = set()
    banned_dict = {}
    
    for banned in banned_ids:
        if banned not in banned_dict:
            banned_dict[banned] = []
        else:
            del banned_dict[banned]
    
    for banned_id in banned_ids:
        for user_id in user_ids:
            if len(banned_id) != len(user_id):
                continue
            flag = True
            for banned, user in zip(banned_id, user_id):
                if banned != '*' and banned != user:
                        flag = False
                        break
            if flag:
                if banned_id in banned_dict:
                    banned_dict[banned_id].append(user_id)

    result = product(*banned_dict.values()) 
    
    for combination in result:
        if len(set(combination)) == len(combination): 
            sorted_combination = tuple(sorted(combination))
            answer.add(sorted_combination)

    return len(answer)
