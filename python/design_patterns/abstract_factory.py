#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Car(object):
    def wroom(self):
        pass


class BMWCar(Car):
    def wroom(self):
        return "BMW: wroom!"


class VWCar(Car):
    def wroom(self):
        return "VW: wroom!"


class CarAbstractFactory(object):
    """ Abstract factory """
    def create_a_car(self):
        pass


class BMWFactory(CarAbstractFactory):
    def create_a_car(self):
        return BMWCar()


class VWFactory(CarAbstractFactory):
    def create_a_car(self):
        return VWCar()


def test():
    from simpletest import _assert
    factory = VWFactory()
    car = factory.create_a_car()
    _assert(car.wroom(), "VW: wroom!")

    factory = BMWFactory()
    car = factory.create_a_car()
    _assert(car.wroom(), "BMW: wroom!")


if __name__ == '__main__':
    test()
