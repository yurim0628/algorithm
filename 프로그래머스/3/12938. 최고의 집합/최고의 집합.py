def solution(n, s):
    if s < n:
        return [-1]
    
    quotient = s // n
    answer = [quotient] * n
   
    remainder = s % n
    for i in range(remainder):
        answer[i] += 1

    return answer[::-1]
