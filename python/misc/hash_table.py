#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpletest import _assert


class _Entry(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self):
        self._buckets = [[] for i in range(64)]

    def __getitem__(self, key):
        index = self._find_bucket(key)
        for entry in self._buckets[index]:
            if entry.key == key:
                return entry.value
        return None

    def __setitem__(self, key, value):
        index = self._find_bucket(key)
        entry = _Entry(key, value)
        self._buckets[index].append(entry)

    def __delitem__(self, key):
        index = self._find_bucket(key)
        for entry in self._buckets[index]:
            if entry.key == key:
                self._buckets[index].remove(entry)

    def _calculate_hash(self, key):
        # SDBM hash algorithm
        _hash = 0
        for c in bytearray(key):
            _hash = c + (_hash << 6) + (_hash << 16) - _hash
        return _hash

    def _find_bucket(self, key):
        return self._calculate_hash(key) % len(self._buckets)


def test():
    ht = HashTable()
    ht['a'] = 1
    _assert(ht['a'], 1)
    _assert(ht['no_such_entry'], None)
    del ht['a']
    _assert(ht['a'], None)
    _assert(ht._buckets, [[] for i in range(64)])
    _assert(ht._find_bucket('mary'), 59)
    _assert(ht._find_bucket('had'), 43)
    _assert(ht._find_bucket('aaa'), 33)
    _assert(ht._find_bucket('little'), 54)
    _assert(ht._find_bucket('lamb'), 42)


if __name__ == '__main__':
    test()
