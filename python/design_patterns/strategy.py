#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Algorithm(object):
    def do(self):
        raise NotImplementedError("Implement this!")


class AlgorithmA(object):
    def do(self):
        print "Solving using AlgorithmA"


class AlgorithmB(object):
    def do(self):
        print "Solving using AlgorithmB"


class ProblemSolver(object):
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self):
        self.strategy.do()

    def change_strategy(self, strategy):
        self.strategy = strategy


def test():
    solver = ProblemSolver(AlgorithmA())
    solver.solve()
    solver.change_strategy(AlgorithmB())
    solver.solve()


if __name__ == '__main__':
    test()
