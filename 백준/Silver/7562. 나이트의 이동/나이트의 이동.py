from collections import deque

def bfs(sx, sy, ex, ey, l, visited):
    directions = [(-2, 1), (-2, -1), (2, 1), (2, -1), 
                  (-1, 2), (1, 2), (-1, -2), (1, -2)]  
    queue = deque([(sx, sy)]) 
    visited[sx][sy] = 1

    while queue:
        cx, cy = queue.popleft()

        if (cx, cy) == (ex, ey):
            return visited[cx][cy] - 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny))

    return -1 

t = int(input())
answers = []
for _ in range(t):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    answers.append(bfs(sx, sy, ex, ey, l, visited))
for answer in answers:
    print(answer)