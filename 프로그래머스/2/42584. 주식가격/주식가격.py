def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i, price in enumerate(prices[1:], 1):
        while stack and prices[stack[-1]] > price:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    while stack:
        index = stack.pop()
        answer[index] = len(prices) - index - 1

    return answer