#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class CarCompany(object):
    has_money = True

    def create_factory(self):
        while self.has_money:
            yield "wrrrooommm... a brand new car rolled out!"


def test():
    from simpletest import _assert, _assert_raises
    gm = CarCompany()
    detroit_factory = gm.create_factory()
    _assert(detroit_factory.next(), "wrrrooommm... a brand new car rolled out!")
    _assert(detroit_factory.next(), "wrrrooommm... a brand new car rolled out!")
    gm.has_money = False
    # No money, no cars
    _assert_raises(StopIteration, detroit_factory.next)
    gm.has_money = True
    # There's money but the factory collapsed.
    _assert_raises(StopIteration, detroit_factory.next)


if __name__ == '__main__':
    test()
