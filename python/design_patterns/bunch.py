#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self


def test():
    from simpletest import _assert
    x = Bunch(name="Mike Tyson", position="Facial plastic surgeon")
    _assert(x.name, "Mike Tyson")

    Node = Bunch
    node = Node(left=Node(left="a", right="b"), right=Node(left="c"))
    _assert(node.left, {'right': 'b', 'left': 'a'})
    _assert(node.left.right, "b")


if __name__ == '__main__':
    test()
