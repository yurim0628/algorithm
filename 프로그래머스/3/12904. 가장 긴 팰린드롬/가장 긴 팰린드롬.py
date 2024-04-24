def solution(s):
    length = len(s)
    if s == s[::-1] or length < 2:
        maxValue = length
    maxValue = 0
    for i in range (length):
        for j in range (length, i, -1):
            tempData = s[i:j]
            if tempData == tempData[::-1]:
                maxValue=max(maxValue, len(tempData))
    

    return maxValue