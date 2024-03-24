def solution(places):
    answer = []
    for place in places:
        arr = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    arr.append((i, j))
        safe = True
        for x1, y1 in arr:
            for x2, y2 in arr:
                distance = abs(x1 - x2) + abs(y1 - y2)
                if distance == 0 or distance > 2:  
                    continue
                elif distance == 1:
                    safe = False  
                    break
                else:
                    if x1 == x2:
                        if place[x1][(y1 + y2) // 2] != 'X':
                            safe = False  
                            break
                    elif y1 == y2:
                        if place[(x1 + x2) // 2][y1] != 'X':
                            safe = False  
                            break
                    else:
                        if place[x1][y2] != 'X' or place[x2][y1] != 'X':  
                            safe = False  
                            break
            if not safe:
                break
        if safe:
            answer.append(1)
        else:
            answer.append(0)
    return answer
