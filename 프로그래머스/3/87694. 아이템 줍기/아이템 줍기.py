from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0 for _ in range(101)] for _ in range(101)]
    
    rectangle = [[x1*2, y1*2, x2*2, y2*2] for x1, y1, x2, y2 in rectangle]
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2+1):
            arr[x][y1], arr[x][y2] = 1, 1
        for y in range(y1, y2+1):
            arr[x1][y], arr[x2][y] = 1, 1
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                if arr[x][y] == 1:
                    arr[x][y] = 0
    
    queue = deque()
    visited = [[0 for _ in range(101)] for _ in range(101)]
    
    sx, sy = characterX*2, characterY*2
    queue.append((sx, sy))
    visited[sx][sy] = 1
    
    while queue:
        cx, cy = queue.popleft()
        
        if (cx, cy) == (itemX*2, itemY*2):
            return visited[cx][cy] // 2
        
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < 101 and 0 <= ny < 101 and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = visited[cx][cy] + 1

    return -1
