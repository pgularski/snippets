#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cached(fun):
    cache = {}
    def wrapped(arg):
        if arg not in cache:
            cache[arg] = fun(arg)
        return cache[arg]
    return wrapped


@cached
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


def fib_counted(n):
    a = 0
    b = 1
    for _ in xrange(n):
        a, b = b, a + b
        # tmp = a
        # a = b
        # b = tmp + b
    return a



def test():
    from simpletest import _assert
    _assert(fib_counted(0), 0)
    _assert(fib_counted(1), 1)
    _assert(fib_counted(2), 1)
    _assert(fib_counted(3), 2)
    _assert(fib_counted(4), 3)
    _assert(fib_counted(42), 267914296)

    _assert(fib(0), 0)
    _assert(fib(1), 1)
    _assert(fib(2), 1)
    _assert(fib(3), 2)
    _assert(fib(4), 3)
    _assert(fib(42), 267914296)


if __name__ == '__main__':
    test()
