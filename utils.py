import copy

def new_board():
    return [[None for i in range(3)] for j in range(3)]

def render(board):
    border_width = (len(board)*2) + 3
    print('   ', '0 1 2')
    print(' ', '-' * border_width)

    for i in range(len(board)):
        print(i, '| ', end='')
        for cell in board[i]:
            if cell == None:
                print(' ', end=' ')
            else:
                print(cell, end=' ')
        print('|')

    print(' ', '-' * border_width)

def get_valid_coordinate(coord_str):
    while True:
        coord = input('=> What is your move\'s {} coordinate? '.format(coord_str))
        if not coord.isdigit() or int(coord) < 0 or int(coord) >= 3:
            print('Invalid coordinate. Please enter a number between 0 and 2.')
        else:
            return int(coord)

def get_valid_move(board):
    x, y = get_valid_coordinate('X'), get_valid_coordinate('Y')
    while board[x][y] != None:
        print('Sorry, ({}, {}) is already taken. Please try again.'.format(x, y))
        x, y = get_valid_coordinate('X'), get_valid_coordinate('Y')
    return (x, y)

def make_move(board, move, player):
    _board = copy.deepcopy(board)
    x, y = move
    _board[x][y] = player
    return _board

def check_for_tie(board):
    if all(board[i][j] is not None \
        for i in range(len(board)) for j in range(len(board[0]))):
        return True
    return False

def check_winning_list(lists, player):
    for lst in lists:
        if all(el == player for el in lst):
            return True
    return False

def get_board_cols(board):
    return [[row[i] for row in board] for i in range(len(board[0]))]

def get_board_diagonals(board):
    diagonals = []
    diagonals.append([r[i] for i, r in enumerate(board)])
    diagonals.append([r[-i-1] for i, r in enumerate(board)])
    return diagonals

def get_winning_lists(board):
    lists_to_check = board.copy()
    lists_to_check.extend(get_board_cols(board))
    lists_to_check.extend(get_board_diagonals(board))
    return lists_to_check

def get_winner(board, player):
    return check_winning_list(get_winning_lists(board), player)

def get_winning_player(board):
    lists = get_winning_lists(board)
    for lst in lists:
        if len(set(lst)) == 1 and lst[0] is not None:
            return lst[0]
    return None

def get_valid_moves(board):
    return [(i, j) for i in range(len(board)) \
            for j in range(len(board[0])) if board[i][j] is None]

