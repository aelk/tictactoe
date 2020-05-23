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

def get_move():
    # TODO write separate validator
    x = input('=> What is your move\'s X co-ordinate? ')
    y = input('=> What is your move\'s Y co-ordinate? ')
    return (x, y)

if __name__ == '__main__':
    board = new_board()
    board[0][1] = 'X'
    board[2][1] = 'O'
    board[0][0] = 'O'
    render(board)

    x, y = get_move()
    print("x =", x)
    print("y =", y)
