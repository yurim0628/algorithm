import sys
from collections import deque

N, M = map(int, input().split())
map = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(sx, sy, wood):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True

    direction = [(-1, 0), (1, 0)] if wood == '|' else [(0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and map[nx][ny] == wood:
                queue.append((nx, ny))
                visited[nx][ny] = True

count = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs(i, j, map[i][j])
            count += 1

print(count)