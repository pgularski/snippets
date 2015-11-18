#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpletest import _assert


def selectionsort(seq):
    for i in range(len(seq) - 1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]


def test():
    seq = [-9, 1, 3, 6, 99, 909]
    selectionsort(seq)
    _assert(seq, [-9, 1, 3, 6, 99, 909])

    seq = []
    selectionsort(seq)
    _assert(seq, [])


if __name__ == '__main__':
    test()
