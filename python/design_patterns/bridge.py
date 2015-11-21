#!/usr/bin/env python
# −*− coding: UTF−8 −*−
"""
The Bridge Pattern allows you to vary the implementation and
the abstraction by placing the two in separate class hierarchies.

"""


# Abstraction
class RemoteController(object):
    """ Abstract RC interface """
    def __init__(self, implementator):
        self._implementator = implementator

    def set_channel(self):
        raise NotImplementedError("Implement this!")


class LogitechRemoteController(RemoteController):
    def set_channel(self, channel):
        self._implementator.tune_channel(channel)


# Implementation
class TV(object):
    def tune_channel(self, channel):
        raise NotImplementedError("Implement this!")


class SonyTV(TV):
    def tune_channel(self, channel):
        print "Sony TV: tunning a channel %s" % channel


def test():
    tv = SonyTV()
    rc = LogitechRemoteController(tv)
    rc.set_channel('Discovery')


if __name__ == '__main__':
    test()
