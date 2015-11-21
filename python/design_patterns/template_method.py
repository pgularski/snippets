#!/usr/bin/env python
# −*− coding: UTF−8 −*−

import abc


class HotBeverage(object):
    __metaclass__ = abc.ABCMeta

    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abc.abstractmethod
    def brew(self):
        """ Implement this """

    @abc.abstractmethod
    def add_condiments(self):
        """ Implement this """

    def boil_water(self):
        print "Boiling water..."

    def pour_in_cup(self):
        print "Pouring..."

    def customer_wants_condiments(self):
        """ Reimplement this if needed. """
        return True


class Coffee(HotBeverage):
    def brew(self):
        print "Preparing cofee..."

    def add_condiments(self):
        print "Adding milk..."


def test():
    Coffee().prepare()


if __name__ == '__main__':
    test()
