def dfs(x, y, digit):
  if len(digit) == 6:
      digit_set.add(digit)
      return

  for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < 5 and 0 <= ny < 5:
          dfs(nx, ny, digit + map_grid[nx][ny])  


map_grid = [input().strip().split() for _ in range(5)]
digit_set = set() 

for i in range(5):
  for j in range(5):
      dfs(i, j, map_grid[i][j])  

print(len(digit_set))