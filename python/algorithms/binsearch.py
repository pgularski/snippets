#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from simpletest import _assert


def binsearch(seq, val):
    l = 0
    h = len(seq) - 1
    mid = (l + h) / 2
    while l < h and seq[mid] != val:
        if val < seq[mid]:
            h = mid - 1
        else:
            l = mid + 1
        mid = (l + h) / 2
    return mid if seq[mid] == val else -1


def test():
    _assert(binsearch([5, 23, 312, 358, 373, 502, 670, 834, 946, 973], 5), 0)
    _assert(binsearch([1, 2, 3], 4), -1)
    _assert(binsearch([1, 2, 3], 0), -1)
    _assert(binsearch([1, 2, 3], -1), -1)
    _assert(binsearch([1, 2, 3], 3), 2)
    _assert(binsearch([-1, 1, 2, 3], -1), 0)


if __name__ == '__main__':
    test()
