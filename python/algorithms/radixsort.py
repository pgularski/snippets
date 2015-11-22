#!/usr/bin/env python
# -*- coding: utf-8 -*-


RADIX = 10


def get_digit(number, digit, base=10):
    return (number / pow(base, digit)) % base


def radixsort(seq):
    max_len_found = False
    pos = -1
    while not max_len_found:
        max_len_found = True
        pos += 1
        buckets = [[] for _ in xrange(RADIX)]
        for i, bucket in enumerate(buckets):
            for value in seq:
                digit = get_digit(value, pos)
                if digit == i:
                    bucket.append(value)
                if digit > 0:
                    max_len_found = False

        seq[:] = [item for bucket in buckets for item in bucket]


def test():
    from simpletest import _assert
    seq = [469, 218, 968, 186, 246, 624, 460, 91, 2, 90, 1015]
    sorted_seq = sorted(seq)

    _assert(seq == sorted_seq, False)
    radixsort(seq)
    _assert(seq == sorted_seq, True)


if __name__ == '__main__':
    test()
