def solution(n, costs):
    graph = {}
    
    for start, end, cost in costs:
        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    
    total_cost = 0
    visited = set()  
    visited.add(0)   
    
    while len(visited) < n:
        min_cost = float('inf')
        next_node = None
        
        for node in visited:
            for neighbor, cost in graph[node]:
                if neighbor not in visited and cost < min_cost:
                    min_cost = cost
                    next_node = neighbor
        
        visited.add(next_node)
        total_cost += min_cost
    
    return total_cost