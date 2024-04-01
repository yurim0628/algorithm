from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    visited = [[0] * m for _ in range(n)]

    def bfs(sx, sy):
        queue = deque([(sx, sy)])
        visited[sx][sy] = 1

        while queue:
            cx, cy = queue.popleft()

            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx, ny = cx + dx, cy + dy

                while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'D':
                    nx, ny = nx + dx, ny + dy

                nx -= dx
                ny -= dy

                if board[nx][ny] == 'G':
                    return visited[cx][cy] 

                if (nx, ny) != (cx, cy) and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
                    
        return -1

    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                result = bfs(x, y)

    return result
