#!/usr/bin/env python
# −*− coding: UTF−8 −*−


@classmethod
def _get_instance(cls, *args, **kargs):
    return cls.__instances.setdefault(
        (args, tuple(kargs.items())),
        super(type(cls), cls).__new__(*args, **kargs))


def flyweight(decoree):
    import weakref
    decoree.__instances = weakref.WeakValueDictionary()
    decoree.__new__ = _get_instance
    return decoree


@flyweight
class Spam(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Foo(Spam):
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

    _assert(s1 is s2, True)
    _assert(s2 is s3, False)

    _assert(f1 is s2, False)
    _assert(f1 is f2, True)
    _assert(f2 is f3, False)


if __name__ == '__main__':
    test()
