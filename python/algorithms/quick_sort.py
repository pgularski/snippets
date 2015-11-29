#!/usr/bin/env python
# -*- coding: utf-8 -*-


def qsort(seq):
    left = []
    right = []
    pivot_values = []
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    for i in seq:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            pivot_values.append(i)
    left = qsort(left)
    right = qsort(right)
    return left + pivot_values + right


def test():
    from simpletest import _assert
    seq = [-9, 1, 3, 6, 99, 909]
    qsort(seq)
    _assert(seq, [-9, 1, 3, 6, 99, 909])

    seq = []
    qsort(seq)
    _assert(seq, [])


if __name__ == '__main__':
    test()
