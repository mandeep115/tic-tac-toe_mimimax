"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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

    X_count = 0
    O_count = 0
    
    if board == initial_state():
        return X
    
    for row in board:
        for box in row:
            if box == X:
                X_count += 1
            elif box == O:
                O_count += 1
            else:
                pass
    return X if O_count>X_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_list.add((i, j))
    return actions_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
     
    # 🔍Checking if action is a legal action
    if action not in actions(board):
        raise Exception("This action does'nt exist")

    # © storing a deep copy of orignal board
    n_board = deepcopy(board)
    # 🙆‍♀️talking to player function for geting next turn
    player_turn = player(board)
    # storing action tuple in i and j
    i, j = action
    # ✅ updating n_board
    n_board[i][j] = player_turn

    return n_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 🔄 Looping 3 and doing some syntactic magic
    for e in range(3):
        # 🚥 for horizontal lines
        if all(board[e][0] == i for i in board[e]) and board[e][0] != EMPTY:
            return board[e][0]
        # 🚦 for vertical lines
        elif board[0][e] == board[1][e] == board[2][e] and board[0][e] != EMPTY:
            return board[0][e]
    # ❌ diagonls
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[0][2]
                
                    ######## CAN BE BETTER!!!!!!!!!!!!!! ##############
    else:
         return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
