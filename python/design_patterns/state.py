#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class State(object):
    def __init__(self, machine):
        self.machine = machine

    def run(self):
        import inspect
        raise NotImplementedError("Implement %s()" % inspect.stack()[0][3])

    def go_idle(self):
        import inspect
        raise NotImplementedError("Implement %s()" % inspect.stack()[0][3])


class IdleState(State):
    def run(self):
        print "Starting machine from idle..."
        self.machine.state = RunState(self.machine)

    def go_idle(self):
        print "Already idle..."


class RunState(State):
    def run(self):
        print "Already running..."

    def go_idle(self):
        print "Going idle..."
        self.machine.state = IdleState(self.machine)


class Machine(object):
    def __init__(self):
        self.state = IdleState(self)

    def run(self):
        self.state.run()

    def go_idle(self):
        self.state.go_idle()


def test():
    machine = Machine()
    machine.run()
    machine.run()
    machine.run()
    machine.go_idle()
    machine.go_idle()
    machine.go_idle()
    machine.run()
    machine.go_idle()


if __name__ == '__main__':
    test()
