#!/usr/bin/env python
# −*− coding: UTF−8 −*−

def fun_a():
    return 'A'


def fun_b():
    return 'B'


def fun_c():
    return 'C'


def fun_default():
    return 'default'


switch = {'a': fun_a,
          'b': fun_b,
          'c': fun_c}


def test():
    from simpletest import _assert
    _assert(switch.get('a', fun_default)(), 'A')
    _assert(switch.get('b', fun_default)(), 'B')
    _assert(switch.get('c', fun_default)(), 'C')
    _assert(switch.get('nonexistent', fun_default)(), 'default')


if __name__ == '__main__':
    test()
