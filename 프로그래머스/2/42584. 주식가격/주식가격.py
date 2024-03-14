def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] 
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)
        
    while stack:
        index = stack.pop()
        answer[index] = n - index - 1

    return answer