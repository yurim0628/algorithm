from collections import deque

N, M, F = map(int, input().split())
arr = [[1]*(N+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]+[[1]*(N+2)]
cx, cy = map(int, input().split())

def bfs_start(cx, cy):
    queue = deque()
    visited = [[0]*(N+2) for _ in range(N+2)]
    texi_list = []
    
    queue.append((cx, cy))
    visited[cx][cy] = 1
    
    while queue:
        new_queue = deque()
        
        for cx, cy in queue:
            if (cx, cy) in start_position:
                texi_list.append([cx, cy])
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = cx + dx, cy + dy
                if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                    new_queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
        
        if len(texi_list) > 0:
            texi_list.sort()
            ex, ey = texi_list[0]
            return ex, ey, visited[ex][ey] - 1 
        
        queue = new_queue
        
    return 0, 0, -1

def bfs_end(sx, sy, ex, ey):
    queue = deque()
    visited = [[0]*(N+2) for _ in range(N+2)]
    
    queue.append((sx, sy))
    visited[sx][sy] = 1
    
    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) == (ex, ey):
            return visited[cx][cy] - 1
        
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + dx, cy + dy
            if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[cx][cy] + 1
                    
    return -1

start_position = set()
dest_position = {}
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    start_position.add((sx, sy))
    dest_position[(sx, sy)] = (ex, ey)
    
for _ in range(M):
    sx, sy, dist = bfs_start(cx, cy)
    if dist == -1 or F < dist:
        F = -1
        break
    F -= dist
    start_position.remove((sx,sy))
    
    ex, ey = dest_position[(sx, sy)]
    dist = bfs_end(sx, sy, ex, ey)
    if dist == -1 or F < dist:
        F = -1
        break
        
    F += dist
    cx, cy = ex, ey

print(F)