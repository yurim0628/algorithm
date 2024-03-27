def get_next_positions(board, loc): 
    next_positions = []
    
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        nx, ny = loc[0] + dx, loc[1] + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 1:
            next_positions.append((nx, ny))
            
    return next_positions

def dfs(board, aloc, bloc, move_count):  
    if move_count % 2 == 0:
        next_positions = get_next_positions(board, aloc)
    else:
        next_positions = get_next_positions(board, bloc)
        
    # 이동 불가능     
    if not next_positions: 
        # 현재 A의 턴이고 A가 진다면 False, 현재 B의 턴이고 B가 진다면 True
        return move_count % 2 == 1, move_count 

    # 이동 후 같은 위치
    if aloc == bloc:  
        # 현재 A의 턴이고 A가 이긴다면 True, 현재 B의 턴이고 B가 이긴다면 False
        return move_count % 2 == 0, move_count + 1

    winning_moves, losing_moves = [], []
    # 현재까지 이동한 횟수가 짝수일 경우 A의 턴임을 의미
    if move_count % 2 == 0:
        ax, ay = aloc[0], aloc[1]
        board[ax][ay] = 0
        for nx, ny in next_positions:
            is_a_win, count = dfs(board, [nx, ny], bloc, move_count + 1)
            if is_a_win:
                winning_moves.append(count)
            else:
                losing_moves.append(count)
        board[ax][ay] = 1     
    # 현재까지 이동한 횟수가 홀수일 경우 B의 턴임을 의미
    else:
        bx, by = bloc[0], bloc[1]
        board[bx][by] = 0 
        for nx, ny in next_positions:
            is_a_win, count = dfs(board, aloc, [nx, ny], move_count + 1)
            if not is_a_win:
                winning_moves.append(count)
            else:
                losing_moves.append(count)
        board[bx][by] = 1 

    if winning_moves: 
        # A가 승리하면 True, B가 승리하면 False 
        # 가장 빠르게 이기는 경우를 반환
        return move_count % 2 == 0, min(winning_moves)                              
    else:                
        # A가 패배하면 False, B가 패배하면 True
        # 최대한 버티는 경우를 반환
        return move_count % 2 == 1, max(losing_moves) 
    
def solution(board, aloc, bloc):
    winner, answer = dfs(board, aloc, bloc, 0)
    return answer