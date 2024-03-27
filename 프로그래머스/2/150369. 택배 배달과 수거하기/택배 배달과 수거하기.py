def solution(cap, n, deliveries, pickups):
    answer = 0
    
    delivery_positions = []
    pickup_positions = []
    for i in range(n):
        if deliveries[i]:
            delivery_positions.append(i)
        if pickups[i]:
            pickup_positions.append(i)
            
    while delivery_positions or pickup_positions:
        d_position = delivery_positions[-1] if delivery_positions else -1
        p_position = pickup_positions[-1] if pickup_positions else -1

        answer += (max(d_position, p_position) + 1) * 2
        
        delivery_cap = cap
        while delivery_positions and delivery_cap > 0:
            position = delivery_positions[-1]
            if delivery_cap >= deliveries[position]:
                delivery_positions.pop()
                delivery_cap -= deliveries[position]
            else:
                deliveries[position] -= delivery_cap
                break
        
        pickup_cap = cap
        while pickup_positions and pickup_cap > 0:
            position = pickup_positions[-1]
            if pickup_cap >= pickups[position]:
                pickup_positions.pop()
                pickup_cap -= pickups[position]
            else:
                pickups[position] -= pickup_cap
                break
        
    return answer
        