from collections import deque

def solution(grid):
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    n = len(grid)
    m = len(grid[0])
    k = 4

    visited = [[[0 for _ in range(k)] for _ in range(m)] for _ in range(n)]

    def bfs(sx, sy, sz):
        count = 1  
        queue = deque([(sx, sy, sz)])
        visited[sx][sy][sz] = 1

        while queue:
            cx, cy, cz = queue.popleft()

            if grid[cx][cy] == 'L':
                nz = (cz - 1) % 4
            elif grid[cx][cy] == 'R':
                nz = (cz + 1) % 4
            else:  
                nz = cz
            dx, dy = direction[nz]
            nx, ny = (cx + dx) % n, (cy + dy) % m

            if not visited[nx][ny][nz]:
                queue.append((nx, ny, nz))
                visited[nx][ny][nz] = 1
                count += 1 

        return count

    answer = []

    for x in range(n):
        for y in range(m):
            for z in range(k):
                if not visited[x][y][z]:
                    answer.append(bfs(x, y, z))

    answer.sort()
    return answer
