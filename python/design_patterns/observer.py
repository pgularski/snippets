#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Subject(object):
    def __init__(self):
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except KeyError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Controller(Subject):
    def __init__(self):
        super(Controller, self).__init__()
        self.name = "data"
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class ListenerA(object):
    def update(self, subject):
        print 'From {0}: Subject "{1}" updated: {2}'.format(
                self.__class__.__name__, subject.name, subject.data)


class ListenerB(object):
    def update(self, subject):
        print 'From {0}: Subject "{1}" updated: {2}'.format(
                self.__class__.__name__, subject.name, subject.data)


def test():
    data = Controller()
    data.attach(ListenerA())
    data.attach(ListenerB())

    data.data = 1

if __name__ == '__main__':
    test()
