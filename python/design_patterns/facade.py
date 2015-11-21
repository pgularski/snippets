#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class A(object):
    def do_a(self):
        print 'Doing a...'


class B(object):
    def do_b(self):
        print 'Doing b...'


class Facade(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do(self):
        self.a.do_a()
        self.b.do_b()


def test():
    f = Facade(A(), B())
    f.do()


if __name__ == '__main__':
    test()
