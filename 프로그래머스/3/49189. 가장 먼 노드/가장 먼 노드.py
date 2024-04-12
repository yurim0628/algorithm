def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    for start, end in edge:
        arr[start].append(end)
        arr[end].append(start)
    
    visited[1] = 1
    queue = [1]
    total_count = 0
    while queue:
        level_count = 0  
        new_queue = []
        for current in queue:
            for next_node in arr[current]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    new_queue.append(next_node)
                    level_count += 1  
                    
        queue = new_queue
        if queue:
            total_count = level_count
    
    return total_count
