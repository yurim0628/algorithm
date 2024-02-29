maxGap = 0
answer = []

def dfs(focus, lscore, ascore, lion, apeach, n):
    global maxGap, answer
    
    # 화살을 다 쏜 경우
    if n == sum(lion):
        if 0 < focus < 10:
            for i in range(focus, 10):
                if apeach[i] != 0:
                    ascore += (10 - i)
        if ascore >= lscore:
            return
        else:
            gap = lscore - ascore
            if gap < maxGap:
                return
            elif gap > maxGap:
                maxGap = gap
                answer.clear()
            answer.append(lion.copy())

    # 화살을 더 많이 쏜 경우
    elif n < sum(lion):
        return
    
    # 화살 덜 쏜 경우
    elif focus == 10:
        lion[focus] = n - sum(lion)
        dfs(-1, lscore, ascore, lion, apeach, n)

    # 화살 쏘기 가능
    else:
        score = 10 - focus

        lion_win = lion.copy()
        lion_win[focus] = apeach[focus] + 1

        # 화살 맞춘 경우
        dfs(focus + 1, lscore + score, ascore, lion_win, apeach, n)

        # 화살 안 맞춘 경우
        if apeach[focus] != 0:
            dfs(focus + 1, lscore, ascore + score, lion, apeach, n)
        else:
            dfs(focus + 1, lscore, ascore, lion, apeach, n)


def solution(n, apeach):
    lion = [0] * len(apeach)
    dfs(0, 0, 0, lion, apeach, n)
    
    if not answer:
        return [-1]
    else:
        if len(answer) == 1:
            return answer[0]
        else:
            min_score = float('inf')
            selected_lion = None
            for l in answer:
                score = sum([l[i] * (10-i) for i in range(11)])
                if score < min_score:
                    min_score = score
                    selected_lion = l
            return selected_lion
