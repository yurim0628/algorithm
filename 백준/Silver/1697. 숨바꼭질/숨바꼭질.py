from collections import deque

N, K = map(int, input().split())

def bfs(start, end):
    if start >= end:
        return start - end

    max_position = 200000  
    queue = deque([start])
    visited = [0] * (max_position + 1)
    visited[start] = 1

    while queue:
        current = queue.popleft()

        if current == end:
            return visited[current] - 1

        for next in (current - 1, current + 1, current * 2):
            if 0 <= next <= max_position and not visited[next]:
                visited[next] = visited[current] + 1
                queue.append(next)

result = bfs(N, K)
print(result)
