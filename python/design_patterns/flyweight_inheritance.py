#!/usr/bin/env python
# −*− coding: UTF−8 −*−

import weakref


class Flyweight(object):
    _instances = weakref.WeakValueDictionary()

    def __init__(self, *args, **kwargs):
        raise NotImplementedError("Implement this!")

    def __new__(cls, *args, **kwargs):
        return cls._instances.setdefault(
            (cls, args, tuple(kwargs.items())),
            super(Flyweight, cls).__new__(cls, *args, **kwargs))


class Spam(Flyweight):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Foo(Spam):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Bar(Foo):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def test():
    from simpletest import _assert
    s1 = Spam(1, 2)
    s2 = Spam(1, 2)
    s3 = Spam(2, 3)

    f1 = Foo(1, 2)
    f2 = Foo(1, 2)
    f3 = Foo(2, 3)

    b1 = Bar(1, 2)
    b2 = Bar(1, 2)
    b3 = Bar(2, 3)

    _assert(s1 is s2, True)
    _assert(s2 is s3, False)
    _assert(f1 is f2, True)
    _assert(f2 is f3, False)
    _assert(b1 is b2, True)
    _assert(b2 is b3, False)


if __name__ == '__main__':
    test()
