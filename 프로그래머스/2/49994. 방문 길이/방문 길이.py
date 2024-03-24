def solution(dirs):
    answer = 0
    
    directions = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    visited = set()
    
    x, y = 0, 0  
    for direction in dirs:
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny

    return len(visited) // 2
