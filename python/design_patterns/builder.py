#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Car(object):
    def __init__(self):
        self._body = None
        self._engine = None
        self._wheels = []
        self._items = []

    def set_body(self, body):
        self._body = body

    def set_engine(self, engine):
        self._engine = engine

    def attach_wheel(self, wheel):
        self._wheels.append(wheel)

    def get_specs(self):
        print "Body: %s" % self._body.name
        print "Engine: %s" % self._engine.power
        print "Wheels: %s" % self._wheels[0].size


class Builder(object):
    def get_body(self):
        raise NotImplementedError("Implement this!")

    def get_engine(self):
        raise NotImplementedError("Implement this!")

    def get_wheel(self):
        raise NotImplementedError("Implement this!")


class FiatBuilder(Builder):
    def get_body(self):
        body = Body()
        body.name = 'hatchback'
        return body

    def get_engine(self):
        engine = Engine()
        engine.power = 100
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel


class Wheel(object):
    size = None


class Engine(object):
    power = None


class Body(object):
    name = None


class Factory(object):
    def set_builder(self, builder):
        self._builder = builder

    def get_car(self):
        car = Car()

        car.set_body(self._builder.get_body())
        car.set_engine(self._builder.get_engine())

        for i in range(4):
            car.attach_wheel(self._builder.get_wheel())

        return car


def test():
    builder = FiatBuilder()
    factory = Factory()
    factory.set_builder(builder)
    car = factory.get_car()
    car.get_specs()


if __name__ == '__main__':
    test()
