def solution(priorities, location):
    arr = []
    answer = 0
    for i, priority in enumerate(priorities):  
        arr.append((i, priority))
        
    while arr:
        if arr[0][1] == max(arr, key=lambda x: x[1])[1]:  
            current = arr.pop(0)  
            answer += 1
            if current[0] == location:
                return answer
        else:
            arr.append(arr.pop(0))  
