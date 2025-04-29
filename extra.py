def board_from_string(string):
    return [list(row.strip()) for row in string.strip().splitlines()]

def display(board):
    n = len(board)
    print('+' + '-' * n + '+')
    print('\n'.join('|'+''.join(row)+'|' for row in board))
    print('+' + '-' * n + '+\n' )

def generate_moves(board, player):
    # Return all available actions from the current state in the form of new_board, actions
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                new_board = [row[:] for row in board] 
                new_board[i][j] = player
                moves.append((new_board, i, j))
  
    return moves

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    n = len(board)
    win_conditions1 = [
        [[(i, j) for j in range(n)] for i in range(n)], # Check rows
        [[(j, i) for j in range(n)] for i in range(n)], # Check columns
    ]
    win_conditions2 = [
        [(i, i) for i in range(n)], # Check \ diagonal
        [(i, (n - 1) - i) for i in range(n)] # Check / diagonal
    ]
    
    for condition in win_conditions1:
        for array in condition:
            if all(board[i][j] == player for (i, j) in array):
                return True
    
    for condition in win_conditions2:
        if all(board[x][y] == player for (x, y) in condition):
            return True
          
    return False

def evaluate(board, player):
    if check_win(board, 'X'):
        return 1 
    if check_win(board, 'O'):
        return -1
    if all(board[i][j] != '.' for i in range(len(board)) for j in range(len(board))):
        return 0  # Draw
    return None  # Not terminal state

def max_value(board, alpha, beta):
    utility = evaluate(board, 'X')
    if utility is not None:
        return utility, None

    value = float('-inf')
    best_move = None

    for new_board, row, col in generate_moves(board, 'X'):
        move_value, _ = min_value(new_board, alpha, beta)
        if move_value > value:
            value = move_value
            best_move = (row, col)
        alpha = max(alpha, value)
        if alpha >= beta:
            break  # Beta cut-off

    return value, best_move

def min_value(board, alpha, beta):
    utility = evaluate(board, 'O')
    if utility is not None:
        return utility, None

    value = float('inf')
    best_move = None

    for new_board, row, col in generate_moves(board, 'O'):
        move_value, _ = max_value(new_board, alpha, beta)
        if move_value < value:
            value = move_value
            best_move = (row, col)
        beta = min(beta, value)
        if alpha >= beta:
            break  # Alpha cut-off

    return value, best_move

def optimal_move(board, player):
    # Return the best move for the player
    if evaluate(board, player) is not None:
        return None
    
    if player == 'X':
        _, best_move = max_value(board, float('-inf'), float('inf'))
    else:
        _, best_move = min_value(board, float('-inf'), float('inf'))

    return best_move

def main():
    board_str = """\
    XX..
    OXO.
    .O..
    X.O.
    """
    board = board_from_string(board_str)
    print(optimal_move(board, 'X'))

main()
