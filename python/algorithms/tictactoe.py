#!/usr/bin/env python
# -*- coding: utf-8 -*-


import termios
import sys
import tty
from itertools import cycle
from collections import defaultdict

SIZE = 3
EMPTY = ' '


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    if char == '\x03':
        raise KeyboardInterrupt
    elif char == '\x04':
        raise EOFError
    return char


def cached(func):
    cache = {}
    def wrapped(self, player, board, alpha, beta):
        player_mark = player.mark
        board_fields = tuple(board.fields.iteritems())
        key = tuple([player_mark, board_fields, alpha, beta])
        if not key in cache:
            cache[key] = func(self, player, board, alpha, beta)
        return cache[key]
    return wrapped


class Board(object):
    def __init__(self, size=3):
        self.size = size
        self.fields = {}
        for y in xrange(size):
            for x in xrange(size):
                self.fields[x, y] = EMPTY
        self.fields_with_mark = defaultdict(set)

    def place_mark(self, mark, x, y):
        self.fields[x, y] = mark
        self.fields_with_mark[mark].add((x, y))

    def empty_fields(self):
        fields_x = self.fields_with_mark['X']
        fields_o = self.fields_with_mark['O']
        all_fields = set(self.fields.keys())
        return all_fields.difference(fields_x.union(fields_o))

    def show(self):
        rows = []
        for y in range(self.size):
            cols = []
            for x in range(self.size):
                cols.append(str(self.fields[x, y]))
            rows.append(' | '.join(cols))
        sep = '\n' + '-' * 3 * self.size + '\n'
        print ''
        print sep.join(rows)
        print ''


class Player(object):
    def __init__(self, mark):
        self.mark = mark
        self.is_ai = False

    def __repr__(self):
        return self.mark

    def move(self, x, y, board):
        board.place_mark(self.mark, x, y)


class Game(object):
    def __init__(self):
        self.board = Board(SIZE)
        self.players = {'X': Player('X'),
                        'O': Player('O')}
        self._next_player = (p for p in cycle(self.players.values()))
        self.current_player = self.next_player()
        self.winning_sequences = self.genarate_winning_sequences()

    @staticmethod
    def genarate_winning_sequences():
        winning_sequences = []
        sequence_l = set()
        sequence_r = set()
        for x in xrange(SIZE):
            sequence_h = set()
            sequence_v = set()
            sequence_l.add((x, x))
            sequence_r.add((x, SIZE - 1 - x))
            for y in xrange(SIZE):
                sequence_h.add((x, y))
                sequence_v.add((y, x))
            winning_sequences.append(sequence_h)
            winning_sequences.append(sequence_v)
        winning_sequences.append(sequence_l)
        winning_sequences.append(sequence_r)
        for i, set_to_froze in enumerate(winning_sequences):
            winning_sequences[i] = frozenset(set_to_froze)
        return frozenset(winning_sequences)

    def next_player(self):
        return self._next_player.next()

    @property
    def other_player(self):
        for player in self.players.values():
            if player is not self.current_player:
                return player

    def get_opponent(self, player_to_check):
        for player in self.players.values():
            if player is not player_to_check:
                return player

    def over(self, board):
        for player in self.players.values():
            if self.win(player, board):
                return True
        if board.empty_fields():
            return False
        return True

    def score(self, player, board):
        if self.win(player, board):
            return 1
        elif self.win(self.get_opponent(player), board):
            return -1
        else:
            return 0

    def win(self, player, board):
        player_marks = board.fields_with_mark[player.mark]
        for seq in self.winning_sequences:
            if seq.issubset(player_marks):
                return True
        return False

    @cached
    def alphabeta(self, player, board, alpha, beta):
        if self.over(board):
            return self.score(self.current_player, board)

        for move in board.empty_fields():
            x, y = move
            player.move(x, y, board)
            opponent = self.get_opponent(player)
            val = self.alphabeta(opponent, board, alpha, beta)
            board.fields[x, y] = EMPTY
            board.fields_with_mark[player.mark].remove((x, y))

            if player is self.current_player:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha

        if player == self.current_player:
            return alpha
        else:
            return beta

    def get_player_move(self):
        valid = [str(x) for x in range(SIZE)]
        while True:
            print 'X: ',
            x = getch()
            print x
            print 'Y: ',
            y = getch()
            print y
            if x in valid and y in valid:
                x = int(x)
                y = int(y)
                if (x, y) in self.board.empty_fields():
                    break
            print '\nInvalid values'
        return x, y

    def get_ai_move(self):
        value = -2
        alpha = -2
        beta = 2
        best_move = None
        for move in self.board.empty_fields():
            x, y = move
            self.current_player.move(x, y, self.board)
            current_value = self.alphabeta(
                self.other_player, self.board, alpha, beta)
            self.board.fields[x, y] = EMPTY
            self.board.fields_with_mark[self.current_player.mark].remove((x, y))
            if current_value > value:
                value = current_value
                best_move = move
            elif current_value == value:
                best_move = move
        x, y = best_move
        return x, y

    def get_next_move(self):
        if self.current_player.is_ai:
            x, y = self.get_ai_move()
        else:
            # x, y = self.get_ai_move()
            x, y = self.get_player_move()
        self.current_player.move(x, y, self.board)
        self.current_player = self.next_player()

    def get_order(self):
        while True:
            print "Who's starting? [A]I/[U]ser?"
            choice = getch()
            if choice in 'Aa':
                self.current_player.is_ai = True
                break
            elif choice in 'Uu':
                self.other_player.is_ai = True
                break

    def print_score(self):
        user = self.current_player
        if self.current_player.is_ai:
            user = self.other_player
        score = self.score(user, self.board)
        if score > 0:
            print 'You win'
        elif score < 0:
            print 'You lose'
        else:
            print 'Tie'

    def run(self):
        self.get_order()
        self.board.show()
        while True:
            if self.over(self.board):
                break
            self.get_next_move()
            self.board.show()
        self.print_score()


def test():
    game = Game()
    assert game.board.empty_fields() != []
    for y in xrange(SIZE):
        for x in xrange(SIZE):
            game.current_player.move(x, y, game.board)
            game.current_player = game.next_player()
    assert game.board.empty_fields() == []
    game.board.show()

    game = Game()
    game.board.fields[0, 0] = 'X'
    game.board.fields[1, 0] = 'X'
    # game.board.fields[2, 0] = 'X'
    assert not game.win(game.players['X'], game.board)
    game.board.fields[0, 0] = 'X'
    game.board.fields[1, 0] = 'X'
    game.board.fields[2, 0] = 'X'
    assert game.win(game.players['X'], game.board)

    game = Game()
    game.board.fields[0, 0] = 'X'
    game.board.fields[1, 1] = 'X'
    # game.board.fields[2, 2] = 'X'
    assert not game.win(game.players['X'], game.board)
    game.board.fields[0, 0] = 'X'
    game.board.fields[1, 1] = 'X'
    game.board.fields[2, 2] = 'X'
    assert game.win(game.players['X'], game.board)

    game = Game()
    game.board.fields[0, 0] = 'X'
    game.board.fields[0, 1] = 'X'
    # game.board.fields[0, 2] = 'X'
    assert not game.win(game.players['X'], game.board)
    game.board.fields[0, 0] = 'X'
    game.board.fields[0, 1] = 'X'
    game.board.fields[0, 2] = 'X'
    assert game.win(game.players['X'], game.board)

    game = Game()
    game.board.fields[0, 0] = 'O'
    game.board.fields[0, 1] = 'O'
    # game.board.fields[0, 2] = 'O'
    assert not game.win(game.players['O'], game.board)
    game.board.fields[0, 0] = 'O'
    game.board.fields[0, 1] = 'O'
    game.board.fields[0, 2] = 'O'
    assert game.win(game.players['O'], game.board)

    assert game.current_player.mark == 'X'
    assert game.other_player.mark == 'O'
    game.current_player = game.next_player()
    assert game.current_player.mark == 'O'
    assert game.other_player.mark == 'X'
    game.current_player = game.next_player()
    assert game.current_player.mark == 'X'
    assert game.other_player.mark == 'O'


def main():
    try:
        import cProfile
        pr = cProfile.Profile()
        pr.enable()
        game = Game()
        game.run()
    finally:
        pr.print_stats(sort=1)

if __name__ == '__main__':
    main()
    # test()
