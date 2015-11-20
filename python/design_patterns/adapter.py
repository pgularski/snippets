#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Duck(object):
    def quack(self):
        return "Quack"

    def fly(self):
        return "I'm flying"


class Turkey(object):
    def gobble(self):
        return "Gobble, gobble"

    def fly(self):
        return "I'm flying a short distance"


class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        return self.turkey.gobble()

    def fly(self):
        return self.turkey.fly()


def test_duck(duck):
    print duck.quack()
    print duck.fly()


def test():
    from simpletest import _assert
    duck = Duck()
    turkey = Turkey()
    turkey_adapter = TurkeyAdapter(turkey)

    test_duck(duck)
    test_duck(turkey_adapter)

    _assert(duck.quack(), "Quack")
    _assert(duck.fly(), "I'm flying")
    _assert(turkey_adapter.quack(), "Gobble, gobble")
    _assert(turkey_adapter.fly(), "I'm flying a short distance")


if __name__ == '__main__':
    test()
