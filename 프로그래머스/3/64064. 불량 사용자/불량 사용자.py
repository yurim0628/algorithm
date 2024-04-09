from itertools import product

def solution(user_id, banned_id):
    answer = set()
    banned_count = {}
    
    
    for banned in banned_id:
        if banned not in banned_count:
            banned_count[banned] = []
        else:
            del banned_count[banned]
            
    if not banned_count: 
        return 1
    
    for banned in banned_id:
        for user in user_id:
            if len(banned) != len(user):
                continue
            flag = True
            for b, u in zip(banned, user):
                if b != '*':
                    if b != u:
                        flag = False
                        break
            if flag:
                if banned in banned_count:
                    banned_count[banned].append(user)

                    
    result = product(*banned_count.values()) 
    unique_combinations = set()  # 중복된 조합을 제거하기 위한 세트
    for combination in result:  
        if len(set(combination)) == len(combination):  # 중복된 조합인지 확인
            unique_combinations.add(combination)
        
    for combination in unique_combinations:
        combination = sorted(combination)
        answer.add(tuple(combination))


    return len(answer)
