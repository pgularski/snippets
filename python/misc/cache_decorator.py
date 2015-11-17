#!/usr/bin/env python
# −*− coding: UTF−8 −*−

import time
import weakref
import collections


def cached_count(func):
    cache = weakref.WeakValueDictionary()
    values = collections.deque(maxlen=64)

    class Val(object):
        def __init__(self, val):
            self.val = val

    def wrapped(val):
        ret = cache.get(val)
        if ret is None:
            # Cannot create weak reference to 'int' object
            ret = cache[val] = Val(func(val))
            values.append(ret)
        return ret.val
    return wrapped


@cached_count
def count(val):
    time.sleep(1)
    return val * 2


LOOPS = 2
for loop in range(LOOPS):
    for i in range(10):
        print count(i)
