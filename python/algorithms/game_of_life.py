#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import time


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wrap(self, id):
        (x, y) = id
        if x < 0:
            x = self.width + x
        if x >= self.width:
            x = x - self.width

        if y < 0:
            y = self.height + y
        if y >= self.height:
            y = y - self.height
        return x, y

    def neighbors(self, id):
        (x, y) = id
        result = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1),
                  (x + 1, y + 1), (x + 1, y - 1),
                  (x - 1, y + 1), (x - 1, y - 1)]
        result = map(self.wrap, result)
        return set(result)

    def nodes(self):
        nodes = set()
        for y in range(self.height):
            for x in range(self.width):
                nodes.add((x, y))
        return nodes


def draw_grid(grid, nodes_alive, width=2):
    def _print(_str):
        fmt = u"{0:<%s}" % width
        _str = fmt.format(_str)
        print(_str, end='')

    for y in range(grid.height):
        for x in range(grid.width):
            if (x, y) in nodes_alive:
                _print(u'●')
                continue
            _print('.')
        print()
    print()


def neighbors_alive(node, grid, nodes_alive):
    neighbors_alive = []
    neighbors = grid.neighbors(node)
    for neighbor in neighbors:
        if neighbor in nodes_alive:
            neighbors_alive.append(neighbor)
    return neighbors_alive


def play(grid, nodes_alive):
    nodes_alive = set(nodes_alive)
    while True:
        draw_grid(grid, nodes_alive)
        to_kill = set()
        to_revive = set()
        for node in grid.nodes():
            if node in nodes_alive:
                # Any live cell with fewer than two live neighbours dies, as if
                # caused by under-population.
                if len(neighbors_alive(node, grid, nodes_alive)) < 2:
                    to_kill.add(node)
                    continue
                # Any live cell with two or three live neighbours lives on to
                # the next generation.
                if 2 <= len(neighbors_alive(node, grid, nodes_alive)) <= 3:
                    continue
                # Any live cell with more than three live neighbours dies, as
                # if by over-population.
                if len(neighbors_alive(node, grid, nodes_alive)) > 3:
                    to_kill.add(node)
                    continue
            else:
                # Any dead cell with exactly three live neighbours becomes a
                # live cell, as if by reproduction.
                if len(neighbors_alive(node, grid, nodes_alive)) == 3:
                    to_revive.add(node)
        nodes_alive -= to_kill
        nodes_alive |= to_revive
        time.sleep(0.2)


def main():
    play(Grid(10, 10), [(0, 0), (1, 0), (2, 0), (2, 0)])


def test():
    from simpletest import _assert
    grid = Grid(10, 10)
    expect = [(0, 1), (0, 9), (1, 0), (1, 1), (1, 9), (9, 0), (9, 1), (9, 9)]
    _assert(grid.neighbors((0, 0)), set(expect))
    expect = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    _assert(grid.neighbors((1, 1)), set(expect))
    expect = [(0, 0), (0, 8), (0, 9), (8, 0), (8, 8), (8, 9), (9, 0), (9, 8)]
    _assert(grid.neighbors((9, 9)), set(expect))
    expect = [(5, 0), (5, 1), (5, 2), (6, 0), (6, 2), (7, 0), (7, 1), (7, 2)]
    _assert(grid.neighbors((6, 1)), set(expect))

    static_block = [(0, 10), (1, 10), (0, 11), (1, 11)]
    oscilator = [(9, 0), (9, 1), (9, 2)]
    glider = [(2, 3), (2, 4), (2, 5), (1, 5), (0, 4)]
    play(Grid(20, 20), static_block + oscilator + glider)


if __name__ == '__main__':
    test()
