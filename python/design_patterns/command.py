#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Light(object):
    def turn_on(self):
        print "Light on..."

    def turn_off(self):
        print "light off..."


class Command(object):
    def __init__(self, target):
        self.target = target

    def execute(self):
        raise NotImplementedError("Implement this!")


class TurnOn(Command):
    def execute(self):
        self.target.turn_on()


class TurnOff(Command):
    def execute(self):
        self.target.turn_off()


class RemoteController(object):
    def __init__(self):
        self._commands = []

    def add(self, command):
        self._commands.append(command)

    def execute(self):
        for cmd in self._commands:
            cmd.execute()


def test():
    cmd1 = TurnOn(Light())
    cmd2 = TurnOff(Light())
    cmd1.execute()
    cmd2.execute()

    rc = RemoteController()
    rc.add(cmd1)
    rc.add(cmd2)
    rc.execute()


if __name__ == '__main__':
    test()
