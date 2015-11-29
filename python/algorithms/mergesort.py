#!/usr/bin/env python
# −*− coding: UTF−8 −*−


def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq) / 2
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])

    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res += (left or right)
    return res


def test():
    from simpletest import _assert
    seq = [-9, 1, 3, 6, 99, 909]
    mergesort(seq)
    _assert(seq, [-9, 1, 3, 6, 99, 909])

    seq = []
    mergesort(seq)
    _assert(seq, [])


if __name__ == '__main__':
    test()
