from collections import deque

R, C = map(int, input().split())
map_grid = [list(input().strip()) for _ in range(R)]

total_ship_count, total_wolf_count = 0, 0
visited = [[False] * C for _ in range(R)]

def bfs(sx, sy):
    global total_ship_count, total_wolf_count
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    ship_count = wolf_count = 0

    while queue:
        cx, cy = queue.popleft()

        if map_grid[cx][cy] == 'k':
            ship_count += 1
        elif map_grid[cx][cy] == 'v':
            wolf_count += 1

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and map_grid[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

    if wolf_count >= ship_count:
        total_wolf_count += wolf_count
    else:
        total_ship_count += ship_count

for i in range(R):
    for j in range(C):
        if map_grid[i][j] in ('v', 'k') and not visited[i][j]:
            bfs(i, j)

print(total_ship_count, total_wolf_count)
