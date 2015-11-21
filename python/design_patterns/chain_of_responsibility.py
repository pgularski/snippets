#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Event(object):
    def __init__(self, name):
        self.name = name


class Widget(object):
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_' + event.name
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)

        elif self.parent:
            self.parent.handle(event)

        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print self.__class__.__name__ + ': ' + event.name

    def handle_default(self, event):
        print 'Default: ' + event.name


class SendDialog(Widget):
    def handle_paint(self, event):
        print self.__class__.__name__ + ': ' + event.name


class MsgText(Widget):
    def handle_down(self, event):
        print self.__class__.__name__ + ': ' + event.name


def test():
    mw = MainWindow()
    sd = SendDialog(mw)
    ms = MsgText(sd)

    down_evt = Event('down')
    paint_evt = Event('paint')
    odd_evt = Event('odd')

    ms.handle(down_evt)
    ms.handle(paint_evt)
    ms.handle(odd_evt)


if __name__ == '__main__':
    test()
