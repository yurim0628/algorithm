from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dungeons in permutations(dungeons, len(dungeons)):
        fatigue, count = k, 0
        for dungeon in dungeons:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                count += 1
        answer = max(answer, count)
    return answer