import os
import copy
import random
import time

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
    updated_board = copy.deepcopy(board)
    x, y = move
    updated_board[x][y] = player
    return updated_board

def play_game():
    board = new_board()
    moves = 0
    while True:
        render(board)
        player = 'X' if moves % 2 == 0 else 'O'
        move = find_winning_and_losing_moves_ai(board, player)
        board = make_move(board, move, player)
        time.sleep(0.2)
        os.system('clear')
        if get_winner(board, player):
            print('Player', player, 'wins!')
            break
        elif check_for_tie(board):
            print('It\'s a tie!')
            break
        moves += 1
    render(board)

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

def get_valid_moves(board):
    return [(i, j) for i in range(len(board)) \
            for j in range(len(board[0])) if board[i][j] is None]

def random_ai(board):
    return random.choice(get_valid_moves(board))

def find_winning_move_helper(board, player):
    valid_moves = get_valid_moves(board)
    board_copy = copy.deepcopy(board)
    for move in valid_moves:
        if get_winner(make_move(board_copy, move, player), player):
            return move
    return None

def find_winning_move_ai(board, player):
    winning_move = find_winning_move_helper(board, player)
    if winning_move is not None:
        return winning_move
    else:
        return random_ai(board)

def find_winning_and_losing_moves_ai(board, player):
    winning_move = find_winning_move_helper(board, player)
    if winning_move is not None:
        return winning_move

    # find winning move for opposite player; if there is one, block it
    blocking_move = find_winning_move_helper(board, 'O' if player == 'X' else 'X')
    if blocking_move is not None:
        return blocking_move

    return random_ai(board)

if __name__ == '__main__':
    play_game()
