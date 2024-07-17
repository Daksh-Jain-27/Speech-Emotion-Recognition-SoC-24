import json
import copy  # use it for deepcopy if needed
import math  # for math.inf
import logging
import pygame

pygame.init()

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)

# Global variables in which you need to store player strategies (this is data structure that'll be used for evaluation)
# Mapping from histories (str) to probability distribution over actions
strategy_dict_x = {}
strategy_dict_o = {}

class History:
    def __init__(self, history=None):
        """
        # self.history : Eg: [0, 4, 2, 5]
            keeps track of sequence of actions played since the beginning of the game.
            Each action is an integer between 0-8 representing the square in which the move will be played as shown
            below.
              ___ ___ ____
             |_0_|_1_|_2_|
             |_3_|_4_|_5_|
             |_6_|_7_|_8_|

        # self.board
            empty squares are represented using '0' and occupied squares are either 'x' or 'o'.
            Eg: ['x', '0', 'x', '0', 'o', 'o', '0', '0', '0']
            for board
              ___ ___ ____
             |_x_|___|_x_|
             |___|_o_|_o_|
             |___|___|___|

        # self.player: 'x' or 'o'
            Player whose turn it is at the current history/board

        :param history: list keeps track of sequence of actions played since the beginning of the game.
        """
        if history is not None:
            self.history = history
            self.board = self.get_board()
        else:
            self.history = []
            self.board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.player = self.current_player()

    def current_player(self):
        """ Player function
        Get player whose turn it is at the current history/board
        :return: 'x' or 'o' or None
        """
        total_num_moves = len(self.history)
        if total_num_moves < 9:
            if total_num_moves % 2 == 0:
                return 'x'
            else:
                return 'o'
        else:
            return None

    def get_board(self):
        """ Play out the current self.history and get the board corresponding to the history in self.board.

        :return: list Eg: ['x', '0', 'x', '0', 'o', 'o', '0', '0', '0']
        """
        board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        for i in range(len(self.history)):
            if i % 2 == 0:
                board[self.history[i]] = 'x'
            else:
                board[self.history[i]] = 'o'
        return board

    def is_win(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for positions in winning_positions:
            if self.board[positions[0]] == self.board[positions[1]] == self.board[positions[2]] != '0':
                return self.board[positions[0]]
        return None

    def is_draw(self):
        return '0' not in self.board and self.is_win() is None

    def get_valid_actions(self):
        return [i for i in range(9) if self.board[i] == '0']

    def is_terminal_history(self):
        return self.is_win() is not None or self.is_draw()

    def get_utility_given_terminal_history(self):
        winner = self.is_win()
        if winner == 'x':
            return 1
        elif winner == 'o':
            return -1
        else:
            return 0

    def update_history(self, action):
        new_history = copy.deepcopy(self.history)
        new_history.append(action)
        return History(new_history)


def backward_induction(history_obj):
    global strategy_dict_x, strategy_dict_o

    if history_obj.is_terminal_history():
        return history_obj.get_utility_given_terminal_history()

    if history_obj.player == 'x':
        best_value = -math.inf
    else:
        best_value = math.inf

    best_action = None

    for action in history_obj.get_valid_actions():
        next_history = history_obj.update_history(action)
        value = backward_induction(next_history)

        if history_obj.player == 'x':
            if value > best_value:
                best_value = value
                best_action = action
        else:
            if value < best_value:
                best_value = value
                best_action = action

    strategy_key = ''.join(map(str, history_obj.history))
    if history_obj.player == 'x':
        strategy_dict_x[strategy_key] = {str(a): 0 for a in range(9)}
        strategy_dict_x[strategy_key][str(best_action)] = 1
    else:
        strategy_dict_o[strategy_key] = {str(a): 0 for a in range(9)}
        strategy_dict_o[strategy_key][str(best_action)] = 1

    return best_value


def solve_tictactoe():
    backward_induction(History())
    with open('./policy_x.json', 'w') as f:
        json.dump(strategy_dict_x, f)
    with open('./policy_o.json', 'w') as f:
        json.dump(strategy_dict_o, f)
    return strategy_dict_x, strategy_dict_o


if __name__ == "__main__":
    logging.info("Start")
    solve_tictactoe()
    logging.info("End")
