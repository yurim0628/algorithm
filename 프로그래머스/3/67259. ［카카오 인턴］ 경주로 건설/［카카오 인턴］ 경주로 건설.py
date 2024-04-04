from collections import deque

def solution(board):
    answer = []

    n = len(board)
    m = len(board[0])

    direction = {'0': [0, 1], '1': [0, -1], '2': [1, 0], '3': [-1, 0]}

    queue = deque()
    visited = [[[float('inf')] * m for _ in range(n)] for _ in range(4)]

    queue.append((0, 0, '0', 0))
    queue.append((0, 0, '2', 0))
    
    visited[0][0][0] = 0
    visited[2][0][0] = 0

    while queue:
        cx, cy, cd, cost = queue.popleft()

        if (cx, cy) == (n-1, m-1):
            answer.append(visited[int(cd)][cx][cy])

        for key, value in direction.items():
            nx, ny = cx + value[0], cy + value[1]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                new_cost = cost + (600 if cd != key else 100)
                if visited[int(key)][nx][ny] > new_cost:
                    visited[int(key)][nx][ny] = new_cost
                    queue.append((nx, ny, key, new_cost))
    answer.sort()
    return answer[0]
