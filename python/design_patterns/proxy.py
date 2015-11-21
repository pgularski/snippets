#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Implementation(object):
    def f(self):
        print "Implementation.f()"

    def g(self):
        print "Implementation.g()"

    def h(self):
        print "Implementation.h()"


class Proxy(object):
    def __init__(self):
        self._implementation = Implementation()

    def __getattr__(self, name):
        return getattr(self._implementation, name)


def test():
    p = Proxy()
    p.f()
    p.g()
    p.h()


if __name__ == '__main__':
    test()
