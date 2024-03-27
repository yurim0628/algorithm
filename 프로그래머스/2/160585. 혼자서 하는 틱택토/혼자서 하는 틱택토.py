def solution(board):
    queue_o = []
    queue_x = []
    count_o = 0
    count_x = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                queue_o.append((i,j))
                count_o += 1
            if board[i][j] == 'X':
                queue_x.append((i,j))
                count_x += 1
                    
    if count_o < count_x or count_o >= count_x + 2:
        return 0
    elif count_o == count_x:
        if is_winning(queue_o): 
            return 0
    elif count_o > count_x:
        if is_winning(queue_x): 
            return 0
    return 1

def is_winning(queue):
    winning_conditions = [
        [(0, 0), (0, 1), (0, 2)], 
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], 
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in winning_conditions:
        if all(cell in queue for cell in condition):
            return True
    return False
