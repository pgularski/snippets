#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from simpletest import _assert


def get_bit(num, bit):
    mask = (1 << bit)
    return (num & mask) != 0


def set_bit(num, bit):
    mask = (1 << bit)
    return num | mask


def clear_bit(num, bit):
    mask = ~(1 << bit)
    return num & mask


def toggle_bit(num, bit):
    mask = 1 << bit
    return num ^ mask


def update_bit(num, bit, val):
    mask = ~(1 << bit)
    return (num & mask) | (val << bit)


def clear_bits_from_bit_up(num, bit):
    mask = (1 << bit) - 1
    return num & mask


def clear_bits_from_bit_down(num, bit):
    mask = ~((1 << (bit + 1)) - 1)
    return num & mask


def _bin(number):
    return bin(number)[2:]


def test():
    _assert(_bin(get_bit(5, 0)), "1")
    _assert(_bin(get_bit(5, 1)), "0")
    _assert(_bin(get_bit(5, 2)), "1")
    _assert(_bin(get_bit(5, 3)), "0")

    _assert(_bin(set_bit(5, 0)), "101")
    _assert(_bin(set_bit(5, 1)), "111")
    _assert(_bin(set_bit(5, 2)), "101")
    _assert(_bin(set_bit(5, 3)), "1101")

    _assert(_bin(clear_bit(5, 0)), "100")
    _assert(_bin(clear_bit(5, 1)), "101")
    _assert(_bin(clear_bit(5, 2)), "1")
    _assert(_bin(clear_bit(5, 3)), "101")

    _assert(_bin(toggle_bit(5, 0)), "100")
    _assert(_bin(toggle_bit(5, 1)), "111")
    _assert(_bin(toggle_bit(5, 2)), "1")
    _assert(_bin(toggle_bit(5, 3)), "1101")

    _assert(_bin(update_bit(5, 0, 0)), "100")
    _assert(_bin(update_bit(5, 0, 1)), "101")
    _assert(_bin(update_bit(5, 1, 0)), "101")
    _assert(_bin(update_bit(5, 1, 1)), "111")
    _assert(_bin(update_bit(5, 2, 0)), "1")
    _assert(_bin(update_bit(5, 2, 1)), "101")
    _assert(_bin(update_bit(5, 3, 0)), "101")
    _assert(_bin(update_bit(5, 3, 1)), "1101")

    _assert(_bin(clear_bits_from_bit_up(5, 0)), "0")
    _assert(_bin(clear_bits_from_bit_up(5, 1)), "1")
    _assert(_bin(clear_bits_from_bit_up(5, 2)), "1")
    _assert(_bin(clear_bits_from_bit_up(5, 3)), "101")

    _assert(_bin(clear_bits_from_bit_down(5, 0)), "100")
    _assert(_bin(clear_bits_from_bit_down(5, 1)), "100")
    _assert(_bin(clear_bits_from_bit_down(5, 2)), "0")
    _assert(_bin(clear_bits_from_bit_down(5, 3)), "0")


if __name__ == '__main__':
    test()
