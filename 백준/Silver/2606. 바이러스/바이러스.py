from collections import deque

def bfs(start, graph, visited):
    count = 0
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                count += 1
                
    return count

computer_count = int(input())
connection_count = int(input())

graph = [[] for _ in range(computer_count + 1)]
visited = [False] * (computer_count + 1)

for _ in range(connection_count):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  

print(bfs(1, graph, visited))