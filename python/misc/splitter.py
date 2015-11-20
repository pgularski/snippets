#!/usr/bin/env python
# −*− coding: UTF−8 −*−

import re
splitter = re.compile(r'(\s+|\S+)' )
# splitter.findall(s)


def test():
    from simpletest import _assert
    expected = ['Mary', ' ', 'had', ' ', 'a', ' ', 'little', ' ', 'lamb']
    _assert(splitter.findall('Mary had a little lamb'),expected)
    _assert(splitter.findall(' '), [' '])
    _assert(splitter.findall(''), [])


if __name__ == '__main__':
    test()
