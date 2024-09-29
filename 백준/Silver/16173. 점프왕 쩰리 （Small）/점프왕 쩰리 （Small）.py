from collections import deque

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        cx, cy = queue.popleft()
        digit = map[cx][cy]
        
        if digit == -1:
            print("HaruHaru")
            return
        
        if cy + digit < N and not visited[cx][cy + digit]:
            visited[cx][cy + digit] = True
            queue.append((cx, cy + digit))
        
        if cx + digit < N and not visited[cx + digit][cy]:
            visited[cx + digit][cy] = True
            queue.append((cx + digit, cy))
    
    print("Hing")

bfs()