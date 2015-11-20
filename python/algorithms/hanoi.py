#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Tower(object):
    def __init__(self, id):
        self.rings = []
        self._id = id

    def add(self, n):
        if self.rings and n >= self.rings[-1]:
            raise ValueError(
                    'Unable to add ring %s to tower %s' % (n, self._id))
        else:
            self.rings.append(n)

    def show(self):
        print self.rings


def move_top_to(source, destination):
    ring = source.rings.pop()
    destination.add(ring)
    print "Moved ring %s from tower %s to towert %s" % \
        (ring, source._id, destination._id)


def move_rings(n, source, destination, spare):
    if n >= 0:
        move_rings(n-1, source, spare, destination)
        move_top_to(source, destination)
        move_rings(n-1, spare, destination, source)


def test():
    from simpletest import _assert
    n = 3
    towers = []
    for i in range(3):
        towers.append(Tower(i))

    for k in reversed(xrange(n)):
        print "Adding ring " + str(k)
        towers[0].add(k)

    _assert(towers[0].rings, [2, 1, 0])
    _assert(towers[1].rings, [])
    _assert(towers[2].rings, [])
    move_rings(n-1, towers[0], towers[2], towers[1])
    _assert(towers[0].rings, [])
    _assert(towers[1].rings, [])
    _assert(towers[2].rings, [2, 1, 0])


if __name__ == '__main__':
    test()
