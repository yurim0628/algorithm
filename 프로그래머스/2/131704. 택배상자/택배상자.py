def solution(order):
    answer = 0
    stack = []
    index = 0
    
    for box_number in range(1, len(order) + 1):
        stack.append(box_number)
        while stack and stack[-1] == order[index]:
            stack.pop()
            index, answer = index + 1, answer + 1 
            
    return answer