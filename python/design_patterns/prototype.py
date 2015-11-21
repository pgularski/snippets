#!/usr/bin/env python
# −*− coding: UTF−8 −*−


from copy import deepcopy


class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        try:
            del self._objects[name]
        except KeyError:
            pass

    def clone(self, name, **attrs):
        obj = deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj


class A(object):
    def __init__(self, name):
        self.name = name

    def f(self):
        print id(self)


def test():
    from simpletest import _assert
    a = A('name A')
    p = Prototype()
    p.register('a', a)
    b = p.clone('a')
    _assert(a.f(), b.f())
    _assert(id(a) == id(b), False)
    _assert(a.name, 'name A')
    _assert(b.name, 'name A')
    p.unregister('a')
    _assert(p._objects, {})
    p.unregister('a')
    _assert(p._objects, {})


if __name__ == '__main__':
    test()
