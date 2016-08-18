__author__ = 'srikanta'
'''
Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
'''

import random
import copy


class GameOfLife(object):
    def next_state(self, cur_state):
        next_state = copy.deepcopy(cur_state)
        rl, cl = len(cur_state), len(cur_state[0])
        for r in xrange(rl):
            for c in xrange(cl):
                state = self.__get_neighbours(r, c, rl, cl, cur_state)
                if state < 2 or state > 3:
                    next_state[r][c] = 0
                if state == 3 and cur_state[r][c] == 0:
                    next_state[r][c] = 1
        return next_state

    def __get_neighbours(self, *args):
        r, c, rl, cl, cs = args[0], args[1], args[2], args[3], args[4]
        tl = [(i,j) for j in xrange(c - 1, c + 2) for i in range(r - 1, r + 2)]
        nb_l = filter(lambda x: x[0] >= 0 and x[0] < rl and x[1] >= 0 and \
                x[1] < cl and (x[0] == r or x[1] == c),tl)
        alive_nb = filter(lambda x: cs[x[0]][x[1]] == 1, nb_l)
        return len(alive_nb)


state = [[random.randint(0, 1) for i in xrange(4)] for j in xrange(4)]
state_case1 = [[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1], [1, 1, 1, 0]]
assert GameOfLife().next_state(state_case1) == [[1, 0, 0, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0]], "Invalid outcome"
