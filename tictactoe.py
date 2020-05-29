import os
import sys
import time
import utils
import bots

def play_game(playerX, playerO):
    board = utils.new_board()
    moves = 0
    while True:
        utils.render(board)
        player = 'X' if moves % 2 == 0 else 'O'
        move = bots.get_ai(playerX if player == 'X' else playerO)(board, player)
        board = utils.make_move(board, move, player)
        #time.sleep(0.2)
        os.system('clear')
        if utils.get_winner(board, player):
            print('Player', player, 'wins!')
            utils.render(board)
            return 1 if player == 'X' else 2
        elif utils.check_for_tie(board):
            print('It\'s a tie!')
            utils.render(board)
            return 0
        moves += 1

def repeated_battle(playerX, playerO):
    rounds = 100
    ties = 0
    playerX_wins, playerO_wins = 0, 0
    for i in range(rounds):
        result = play_game(playerX, playerO)
        if result == 0: ties += 1
        elif result == 1: playerX_wins += 1
        else: playerO_wins += 1
    print("ties:", ties)
    print("playerX wins:", playerX_wins)
    print("playerO wins:", playerO_wins)

if __name__ == '__main__':
    playerX, playerO = sys.argv[1], sys.argv[2]
    repeated_battle(playerX, playerO)
    #board = new_board()
    #minimax_score(board, 'O', 'X')
