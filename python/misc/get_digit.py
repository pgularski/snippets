#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_digit(number, digit, base=10):
    return (number / pow(base, digit)) % base


def test():
    from simpletest import _assert
    _assert(get_digit(123, 0), 3)
    _assert(get_digit(123, 1), 2)
    _assert(get_digit(123, 2), 1)
    _assert(get_digit(123, 3), 0)

    _assert(get_digit(5, 0, 2), 1)
    _assert(get_digit(5, 1, 2), 0)
    _assert(get_digit(5, 2, 2), 1)
    _assert(get_digit(5, 3, 2), 0)


if __name__ == '__main__':
    test()
