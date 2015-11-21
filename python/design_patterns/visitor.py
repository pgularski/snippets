#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Node(object):
    def __init__(self):
        self.children = []

    def add(self, node):
        self.children.append(node)

    def do(self):
        print 'Node'

    def accept(self, visitor):
        visitor.visit(self)


class NodeA(Node):
    def do(self):
        print "NodeA"


class NodeB(Node):
    def do(self):
        print "NodeB"


class Visitor():
    def visit(self, node):
        node.do()
        for child in node.children:
            child.accept(self)


def test():
    root = Node()
    node_a = NodeA()
    node_b = NodeB()

    root.add(node_a)
    root.add(node_b)
    node_a.add(node_b)

    visitor = Visitor()
    visitor.visit(root)


if __name__ == '__main__':
    test()
