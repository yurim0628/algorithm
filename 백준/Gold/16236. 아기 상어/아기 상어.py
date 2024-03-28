from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def setup(shark_x, shark_y):
  shark_queue = deque()
  visited = [[0] * n for _ in range(n)]

  shark_queue.append((shark_x, shark_y))
  visited[shark_x][shark_y] = 1

  fish_list = []
  return shark_queue, visited, fish_list
  
def bfs(shark_x, shark_y):
  total_time = 0
  shark_eat, shark_size = 0, 2
  
  flag = False
  
  shark_queue, visited, fish_list = setup(shark_x, shark_y)

  while shark_queue:
    new_shark_queue = deque()

    for cx, cy in shark_queue:
       for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
         nx, ny = cx + dx, cy + dy
         if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
           if arr[nx][ny] < shark_size and arr[nx][ny] != 0:
             fish_list.append((nx, ny))
             visited[nx][ny] = visited[cx][cy] + 1
             flag = True
           if arr[nx][ny] == 0 or arr[nx][ny] == shark_size:
             new_shark_queue.append((nx, ny))
             visited[nx][ny] = visited[cx][cy] + 1
             
    shark_queue = new_shark_queue
    
    if flag:
      shark_x, shark_y = sorted(fish_list)[0]
      arr[shark_x][shark_y] = 0
      total_time += (visited[shark_x][shark_y] - 1)
    
      shark_eat += 1
      if shark_size == shark_eat:
        shark_size += 1
        shark_eat = 0

      flag = False

      shark_queue, visited, fish_list = setup(shark_x, shark_y)
      
  return total_time

shark_x, shark_y = 0, 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 9:
            arr[x][y] = 0
            shark_x, shark_y = x, y
            break

print(bfs(shark_x, shark_y))
