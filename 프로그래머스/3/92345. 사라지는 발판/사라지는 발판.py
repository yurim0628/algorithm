def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    
    def minimax(aloc, bloc):
        cx, cy = aloc[0], aloc[1]
        
        if board[cx][cy] == 0:
            return 0
        
        possible_moves = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[cx][cy] = 0
                possible_moves.append(1 + minimax(bloc, (nx, ny)))
                board[cx][cy] = 1
        
        # minmax algorithm
        best_move = 0
        for move in possible_moves: 
            if move % 2 == 1:  # 현재 플레이어가 이기고 있는 경우
                if best_move % 2 == 0:  # 이전에는 졌는데 현재는 이긴 경우 
                    best_move = move
                if best_move % 2 == 1:  # 이전에도 이기고 현재도 이긴 경우
                    best_move = min(best_move, move)  # 더 빠르게 이길 수 있는 경우 선택
            if move % 2 == 0:  # 현재 플레이어가 지고 있는 경우
                if best_move % 2 == 0:  # 이전에도 졌는데 현재도 진 경우
                    best_move = max(move, best_move)  # 최대한 늦게 질 수 있는 경우 선택
        
        return best_move 
    
    return minimax(aloc, bloc)
