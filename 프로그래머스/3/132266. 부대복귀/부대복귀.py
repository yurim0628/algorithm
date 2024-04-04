from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    arr = [[] for _ in range(n + 1)]
    for destination_a, destination_b in roads:
        arr[destination_a].append(destination_b)
        arr[destination_b].append(destination_a)
        
    queue = deque()
    visited = [-1] * (n + 1)
    
    queue.append(destination)
    visited[destination] += 1
    
    while queue:
        current_destination = queue.popleft()
        
        for next_destination in arr[current_destination]:
            if visited[next_destination] == -1:
                queue.append(next_destination)
                visited[next_destination] = visited[current_destination] + 1
    
    for source in sources:
        if source == destination:
            answer.append(0)
        else:
            answer.append(visited[source])
    
    return answer
