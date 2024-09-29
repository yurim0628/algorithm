R, C = map(int, input().split())

map = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

count = 0
queue = []

def bfs(i, j):
  queue = [(i, j)]
  while queue:
    cx, cy = queue.pop()
    for dx, dy in [(1, 0), (0, 1)]:
      nx, ny = cx + dx, cy + dy
      if 0 <= nx < R and 0 <= ny < C and map[nx][ny] == '#' and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx, ny))

for i in range(R):
  for j in range(C):
    if map[i][j] == '#' and not visited[i][j]:
      visited[i][j] = True
      bfs(i, j)
      count += 1

print(count)