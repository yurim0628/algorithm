def solution(order):
    answer = 0
    stack = []
    box_number = 1
    i = 0
    
    while box_number != len(order) + 1:
        stack.append(box_number)
        while stack and stack[-1] == order[i]:
            stack.pop()
            i += 1
            answer += 1
        box_number += 1
    return answer