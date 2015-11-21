#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from collections import defaultdict


class Mediator(object):
    def __init__(self):
        self.signals = defaultdict(set)

    def signal(self, signal_name, *args, **kwargs):
        for listener in self.signals[signal_name]:
            listener.notify(*args, **kwargs)

    def connect(self, signal_name, listener):
        self.signals[signal_name].add(listener)

    def disconnect(self, signal_name, listener):
        try:
            self.signals[signal_name].remove(listener)
        except KeyError:
            pass


class Listener(object):
    def notify(self, *args, **kwargs):
        print self.__class__.__name__, args, kwargs


class A(Listener):
    pass


class B(Listener):
    pass


class C(Listener):
    pass


class D(Listener):
    pass


sig1 = 'sig1'
sig2 = 'sig2'


a = A()
b = B()
c = C()
d = D()


def test():
    m = Mediator()
    m.connect(sig1, a)
    m.connect(sig1, b)
    m.connect(sig2, c)
    m.connect(sig2, d)
    m.signal(sig1, 'signal A')
    m.signal(sig2, 'signal B')
    m.disconnect(sig1, b)
    m.signal(sig1, 'signal A', kwarg="Ain't nobody got time for that")
    m.disconnect(sig1, b)


if __name__ == '__main__':
    test()
