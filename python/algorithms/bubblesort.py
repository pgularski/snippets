#!/usr/bin/env python
# −*− coding: UTF−8 −*−


def bubblesort(seq):
    for i in range(1, len(seq)):
        for j in range(1, len(seq)):
            if seq[j - 1] > seq[j]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]


def test():
    from simpletest import _assert
    seq = [-9, 1, 3, 6, 99, 909]
    bubblesort(seq)
    _assert(seq, [-9, 1, 3, 6, 99, 909])

    seq = []
    bubblesort(seq)
    _assert(seq, [])


if __name__ == '__main__':
    test()
