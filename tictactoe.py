import os

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
        move = get_valid_move(board)
        board = make_move(board, move, 'X' if moves % 2 == 0 else 'O')
        if get_winner(board):
            render(board)
            break
        os.system('clear')
        moves += 1

def get_winner(board):
    for row in board:
        if all(el == row[0] and el is not None for el in row):
            print('Player', row[0], 'wins!')
            return True

    for i in range(len(board[0])):
        if all(board[j][i] == board[0][i] and board[j][i] is not None \
            for j in range(len(board))):
            print('Player', board[0][i], 'wins!')
            return True

    if (all(board[i][i] == board[0][0] and board[i][i] is not None \
        for i in range(3))) or \
        board[0][2] == board[1][1] == board[2][0] != None:
        print('Player', board[1][1], 'wins!')
        return True

    return False

if __name__ == '__main__':
    play_game()
