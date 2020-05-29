import copy
import random
import utils

def get_ai(player):
    player_name_to_ai = {
        'random_ai': random_ai,
        'find_winning_move_ai': find_winning_move_ai,
        'find_winning_and_losing_moves_ai': find_winning_and_losing_moves_ai,
        'minimax_ai': minimax_ai
    }
    if player in player_name_to_ai:
        return player_name_to_ai[player]
    else:
        return random_ai

def random_ai(board, player):
    return random.choice(utils.get_valid_moves(board))

def find_winning_move_helper(board, player):
    valid_moves = utils.get_valid_moves(board)
    _board = copy.deepcopy(board)
    for move in valid_moves:
        if utils.get_winner(make_move(_board, move, player), player):
            return move
    return None

def find_winning_move_ai(board, player):
    winning_move = find_winning_move_helper(board, player)
    if winning_move is not None:
        return winning_move
    else:
        return random_ai(board, player)

def find_winning_and_losing_moves_ai(board, player):
    winning_move = find_winning_move_helper(board, player)
    if winning_move is not None:
        return winning_move

    # find winning move for opposite player; if there is one, block it
    blocking_move = find_winning_move_helper(board, 'O' if player == 'X' else 'X')
    if blocking_move is not None:
        return blocking_move

    return random_ai(board, player)

def minimax_score(board, player_to_move, player_to_optimize, cache={}):
    board_cache_key = str(board)
    if board_cache_key in cache:
        return cache[board_cache_key]

    winner = utils.get_winning_player(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        elif winner == player_to_move:
            return -10
    elif utils.check_for_tie(board):
        return 0

    valid_moves = utils.get_valid_moves(board)
    scores = []
    for move in valid_moves:
        _board = copy.deepcopy(board)
        _board = utils.make_move(_board, move, player_to_move)
        opponent = 'O' if player_to_move == 'X' else 'X'
        score = minimax_score(_board, opponent, player_to_optimize, cache)
        scores.append(score)

    if player_to_move == player_to_optimize:
        cache[board_cache_key] = max(scores) if len(scores) > 0 else -10
    else:
        cache[board_cache_key] = min(scores) if len(scores) > 0 else 10

    return cache[board_cache_key]

def minimax_ai(board, player):
    valid_moves = utils.get_valid_moves(board)
    best_move = None
    best_score = None
    for move in valid_moves:
        _board = copy.deepcopy(board)
        utils.make_move(_board, move, player)
        opponent = 'O' if player == 'X' else 'X'
        score = minimax_score(_board, opponent, player)
        if best_score is None or score > best_score:
            best_move = move
            best_score = score
    return best_move
