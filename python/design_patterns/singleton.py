#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls, *args, **kwargs)
        return cls._the_instance


class A(Singleton):
    def __init__(self):
        self.x = 'X'


def test():
    from simpletest import _assert
    a = A()
    b = A()
    _assert(a is b, True)

    _assert(a.x, 'X')
    a.x = 'Y'
    _assert(b.x, 'Y')


if __name__ == '__main__':
    test()
