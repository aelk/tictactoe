import os
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
    updated_board = board.copy()
    x, y = move
    updated_board[x][y] = player
    return updated_board

def play_game():
    board = new_board()
    moves = 0
    while True:
        render(board)
        move = random_ai(board) #get_valid_move(board)
        player = 'X' if moves % 2 == 0 else 'O'
        board = make_move(board, move, player)
        time.sleep(0.2)
        os.system('clear')
        if get_winner(board, player) or check_for_tie(board):
            render(board)
            break
        moves += 1

def check_for_tie(board):
    if all(board[i][j] is not None \
        for i in range(len(board)) for j in range(len(board[0]))):
        print('It\'s a tie!')
        return True
    return False

def check_winning_list(lists, player):
    for lst in lists:
        if all(el == player for el in lst):
            print('Player', player, 'wins!')
            return True
    return False

def get_board_cols(board):
    return [[row[i] for row in board] for i in range(len(board[0]))]

def get_board_diagonals(board):
    diagonals = []
    diagonals.append([r[i] for i, r in enumerate(board)])
    diagonals.append([r[-i-1] for i, r in enumerate(board)])
    return diagonals

def get_winner(board, player):
    lists_to_check = board.copy()
    lists_to_check.extend(get_board_cols(board))
    lists_to_check.extend(get_board_diagonals(board))
    return check_winning_list(lists_to_check, player)

def random_ai(board):
    valid_moves = [(i, j) for i in range(len(board)) \
                    for j in range(len(board[0])) if board[i][j] is None]
    return random.choice(valid_moves)

def winning_move_ai(board, player):
    # TODO
    return None

if __name__ == '__main__':
    play_game()
