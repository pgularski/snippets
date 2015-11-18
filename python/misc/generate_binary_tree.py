#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpletest import _assert


class Node(object):
    def __init__(self):
        self.left = None
        self.right = None


def get_tree(depth=0):
    if depth <= 0:
        return None
    node = Node()
    node.left = get_tree(depth-1)
    node.right = get_tree(depth-1)
    return node


def test():
    _assert(get_tree(depth=-1), None)
    _assert(get_tree(depth=0), None)
    _assert(isinstance(get_tree(depth=1), Node), True)
    _assert(get_tree(depth=1).left, None)
    _assert(get_tree(depth=1).right, None)
    _assert(isinstance(get_tree(depth=2), Node), True)
    _assert(isinstance(get_tree(depth=2).left, Node), True)
    _assert(isinstance(get_tree(depth=2).right, Node), True)
    _assert(get_tree(depth=2).left.left, None)
    _assert(get_tree(depth=2).left.right, None)
    _assert(get_tree(depth=2).right.left, None)
    _assert(get_tree(depth=2).right.right, None)


if __name__ == '__main__':
    test()
