def new_board():
    return [[None for i in range(3)] for j in range(3)]

def render(board):
    border_width = (len(board)*2) + 3
    print('-' * border_width)

    for row in board:
        print('| ', end='')
        for cell in row:
            if cell == None:
                print(' ', end=' ')
            else:
                print(cell, end=' ')
        print('|')

    print('-' * border_width)

if __name__ == '__main__':
    board = new_board()
    board[0][1] = 'X'
    board[2][1] = 'O'
    board[0][0] = 'O'
    render(board)
