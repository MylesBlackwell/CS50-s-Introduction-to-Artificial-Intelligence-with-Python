"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Count the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # If X has more moves, it's O's turn; if O has more moves, it's X's turn; if equal, it's X's turn
    if x_count > o_count:
        return O
    elif x_count < o_count:
        return X
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    available_actions = set()

    # Find all empty cells on the board
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                available_actions.add((i, j))
            
    return available_actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if the action is valid
    if action not in actions(board):
        raise ValueError("Invalid action")

    # Get the coordinates of the action
    i, j = action
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    new_board[i][j] = player(board)  # Place the player's mark
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If there's a winner, the game is over
    if winner(board) is not None:
        return True
    
    # If there are any empty cells, the game is not over
    for row in board:
        if EMPTY in row:
            return False
        
    return True  # No empty cells and no winner means it's a draw

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Determine the winner
    win = winner(board)

    # Return the appropriate utility value
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0 
    
    raise NotImplementedError


def maxValue(board):
    """
    Returns the maximum utility value for the maximizing player (X).
    """

    # If the game is over, return the utility value
    if terminal(board):
        return utility(board)

    v = -math.inf  # Initialize v to negative infinity

    # for each possible action, calculate the minimum value of the resulting board and update v
    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v


def minValue(board):
    """
    Returns the minimum utility value for the minimizing player (O).
    """

    # If the game is over, return the utility value
    if terminal(board):
        return utility(board)

    # Initialize v to positive infinity
    v = math.inf

    # For each possible action, calculate the maximum value of the resulting board and update v
    for action in actions(board):
        if action is not None:
            v = min(v, maxValue(result(board, action)))
    return v 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    current_player = player(board)  # Determine the current player

    # If the game is over, return None
    if terminal(board):
        return None
    
    best_action = None  # Initialize best_action to None

    # choose the action that maximizes the minimum value for X or minimizes the maximum value for O
    if current_player == X:
        for action in actions(board):
            if best_action is None:
                best_action = action
            if minValue(result(board, action)) > minValue(result(board, best_action)):
                best_action = action
    else:
        for action in actions(board):
            if best_action is None:
                best_action = action
            if maxValue(result(board, action)) < maxValue(result(board, best_action)):
                best_action = action
            
    return best_action
    raise NotImplementedError
