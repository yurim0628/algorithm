from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)
    current_weight = 0 
    answer = 0
    
    truck_weights = truck_weights[::-1]  
    
    while truck_weights:
        current_weight -= queue.popleft()
        
        if current_weight + truck_weights[-1] <= weight:
            truck_weight = truck_weights.pop()
            queue.append(truck_weight)
            current_weight += truck_weight
        else:
            queue.append(0)
        
        answer += 1
    
    answer += bridge_length  
    
    return answer
