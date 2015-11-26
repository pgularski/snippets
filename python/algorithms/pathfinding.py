#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import random
from Queue import deque, PriorityQueue


left_arrow = u'←'
right_arrow = u'→'
up_arrow = u'↑'
down_arrow = u'↓'


class NodesPriorityQueue(object):
    def __init__(self):
        self.queue = PriorityQueue()

    def empty(self):
        return self.queue.empty()

    def put(self, item, priority):
        self.queue.put((priority, item))

    def get(self):
        return self.queue.get()[1]


class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def can_pass(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        result = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        if (x + y) % 2 == 0: result.reverse()
        # if (x + y) % 2 == 0: random.shuffle(result)
        result = filter(self.in_bounds, result)
        result = filter(self.can_pass, result)
        return result


class WeightedGrid(Grid):
    def __init__(self, width, height):
        super(WeightedGrid, self).__init__(width, height)
        self.weights = {}

    def cost(self, a, b):
        return self.weights.get(b, 1)


def get_direction(point, parents):
    x, y = point
    if parents[point] == (x + 1, y):
        return right_arrow
    if parents[point] == (x - 1, y):
        return left_arrow
    if parents[point] == (x, y - 1):
        return up_arrow
    if parents[point] == (x, y + 1):
        return down_arrow


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path


def draw_grid(graph, width=2, point_to=None, number=None, path=None,
        start=None, goal=None):
    def _print(_str):
        fmt = u"{0:<%s}" % width
        _str = fmt.format(_str)
        print(_str, end='')

    for y in range(graph.height):
        for x in range(graph.width):
            if number and (x, y) in number:
                _print(unicode(number[(x, y)]))
                continue
            if (x, y) == start:
                _print(u'A')
                continue
            if (x, y) == goal:
                _print(u'Z')
                continue
            if path and (x, y) in path:
                _print(u'●')
                continue
            if (x, y) in graph.walls:
                _print(u'##')
                continue
            if point_to and (x, y) in point_to:
                _print(get_direction((x, y), point_to))
                continue
            _print('.')
        print()


def breadth_first_search(graph, start, goal):
    border = deque()
    border.append(start)
    came_from = {}
    came_from[start] = None
    while border:
        current = border.popleft()
        if current == goal:
            break
        for node in graph.neighbors(current):
            if node not in came_from:
                border.append(node)
                came_from[node] = current
    return came_from


def dijstra_search(graph, start, goal):
    border = NodesPriorityQueue()
    border.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while border:
        current = border.get()
        if current == goal:
            break
        for node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, node)
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node] = new_cost
                priority = new_cost
                border.put(node, priority)
                came_from[node] = current
    return came_from, cost_so_far


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    border = NodesPriorityQueue()
    border.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while border:
        current = border.get()
        if current == goal:
            break
        for node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, node)
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node] = new_cost
                priority = new_cost + heuristic(goal, node)
                border.put(node, priority)
                came_from[node] = current
    return came_from, cost_so_far


def get_wall(top_left, bottom_right):
    tlx, tly = top_left
    brx, bry = bottom_right
    return [(x, y) for y in range(tly, bry + 1) for x in range(tlx, brx + 1)]


def test():
    WALL_A = get_wall((4, 4), (5, 11))
    WALL_B = get_wall((14, 5), (15, 14))
    WALL_C = get_wall((22, 0), (23, 6))
    WALL_D = get_wall((24, 5), (26, 6))
    WALL_E = get_wall((14, 0), (15, 3))
    WALL_F = get_wall((1, 4), (4, 4))
    WALL_G = get_wall((1, 11), (4, 11))
    WALL = WALL_A + WALL_B + WALL_C + WALL_D + WALL_E + WALL_F + WALL_G

    start = (3, 8)
    goal = (28, 3)
    print('Breadth first search:')
    grid = Grid(30, 15)
    grid.walls.extend(WALL)
    # draw_grid(grid)
    parents = breadth_first_search(grid, start, goal)
    print(len(reconstruct_path(parents, start, goal)))
    draw_grid(grid, point_to=parents, start=start, goal=goal,
            path=reconstruct_path(parents, start, goal))

    print('Dijkstra search:')
    grid = WeightedGrid(30, 15)
    grid.walls.extend(WALL)
    grid.weights[(12, 4)] = 20
    parents, cost = dijstra_search(grid, start, goal)
    print(len(reconstruct_path(parents, start, goal)))
    draw_grid(grid, point_to=parents, start=start, goal=goal,
            path=reconstruct_path(parents, start, goal))

    print('Dijkstra search cost:')
    draw_grid(grid, width=3, number=cost, start=start, goal=goal,
            path=reconstruct_path(parents, start, goal))

    print('A* search:')
    grid = WeightedGrid(30, 15)
    grid.walls.extend(WALL)
    grid.weights[(12, 4)] = 20
    parents, cost = a_star_search(grid, start, goal)
    print(len(reconstruct_path(parents, start, goal)))
    draw_grid(grid, point_to=parents, start=start, goal=goal,
            path=reconstruct_path(parents, start, goal))

    print('A* search cost:')
    draw_grid(grid, width=3, number=cost, start=start, goal=goal,
            path=reconstruct_path(parents, start, goal))


if __name__ == '__main__':
    test()
