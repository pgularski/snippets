#!/usr/bin/env python
# -*- coding: utf-8 -*-


import termios
import sys
import tty


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    if char == '\x03':
        raise KeyboardInterrupt
    elif char == '\x04':
        raise EOFError
    return char


def test():
    print "Press a key: ",
    char = getch()
    print
    print "You pressed '{0}'".format(char)


if __name__ == '__main__':
    test()
