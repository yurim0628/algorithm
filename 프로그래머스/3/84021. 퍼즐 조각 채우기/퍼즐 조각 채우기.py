from collections import deque

def rotate_90(puzzle):
    rotated_puzzle = []
    
    for x, y in puzzle:
        rotated_puzzle.append((y, len(puzzle) - 1 - x))
        
    return rotated_puzzle

def find_puzzle_pieces(sx, sy, table, visited, n, m):
    puzzle_pieces = []
    
    queue = deque()
    visited[sx][sy] = 1
    queue.append((sx,sy))
    
    while queue:
        cx, cy = queue.popleft()
        puzzle_pieces.append((cx,cy))
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                
    return puzzle_pieces

def find_empty_spaces(sx, sy, game_board, visited, n, m):
    empty_spaces = []
    
    queue = deque()
    visited[sx][sy] = 1
    queue.append((sx,sy))
    
    while queue:
        cx, cy = queue.popleft()
        empty_spaces.append((cx, cy))
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and game_board[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                  
    return empty_spaces

def check(empty_space, puzzle):
    sorted_empty_space = sorted(empty_space)
    sorted_puzzle = sorted(puzzle)
    
    for i in range(len(sorted_empty_space) - 1):
        ex = sorted_empty_space[i+1][0] - sorted_empty_space[i][0]
        ey = sorted_empty_space[i+1][1] - sorted_empty_space[i][1]
        
        px = sorted_puzzle[i+1][0] - sorted_puzzle[i][0]
        py = sorted_puzzle[i+1][1] - sorted_puzzle[i][1]
        
        if (ex != px) or (ey != py):
            return False
    
    return True

def solution(game_board, table):
    answer = 0
    
    n = len(game_board)
    m = len(game_board[0])
    
    puzzle_list = []
    visited = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if table[x][y] == 1 and visited[x][y] == 0:
                puzzle = find_puzzle_pieces(x, y, table, visited, n, m)
                puzzle_list.append(puzzle)
    
    visited = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if game_board[x][y] == 0 and visited[x][y] == 0:
                flag = False
                empty_space = find_empty_spaces(x, y, game_board, visited, n, m)
                for index, puzzle in enumerate(puzzle_list):
                    if len(empty_space) == len(puzzle):
                        for _ in range(4):
                            if check(empty_space, puzzle):
                                flag = True
                                answer += len(puzzle)
                                break
                            puzzle = rotate_90(puzzle) 
                        
                        if flag:
                            puzzle_list.pop(index)
                            break
    return answer
