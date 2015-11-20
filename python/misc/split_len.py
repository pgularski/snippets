#!/usr/bin/env python
# -*- coding: utf-8 -*-


def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]


def test():
    from simpletest import _assert
    _assert(split_len('A', 2), ['A'])
    _assert(split_len('ABC', 2), ['AB', 'C'])
    _assert(split_len('ABCASDF', 2), ['AB', 'CA', 'SD', 'F'])
    _assert(split_len('', 2), [])
    _assert(split_len([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
    _assert(split_len('ABC', 1), ['A', 'B', 'C'])


if __name__ == '__main__':
    test()
