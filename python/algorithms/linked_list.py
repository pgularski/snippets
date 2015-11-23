#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return "{0}→".format(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        cur = self.head
        if cur is None:
            return "<empty>"
        out = []
        while cur:
            out.append(repr(cur))
            cur = cur.next_node
        return "".join(out)

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next_node

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("list indices must be integers, not {0}".format(
                index.__class__.__name__))
        for i, value in enumerate(self):
            if i == index:
                return value
        raise IndexError("list index out of range")

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def index(self, value):
        cur = self.head
        index = 0
        while cur:
            if cur.value == value:
                return index
            cur = cur.next_node
            index += 1
        msg = "{0} is not in list".format(value)
        raise ValueError(msg)

    def pop(self):
        # Case: Empty list
        if self.head is None:
            raise IndexError("pop from empty list")
        prev = self.head
        cur = self.head.next_node
        # Case: One element left
        if not cur:
            node = self.head
            self.head = None
            self.tail = None
            return node
        # Case: More than one element left in the list
        while cur and cur.next_node:
            prev = cur
            cur = cur.next_node
        node = prev.next_node
        prev.next_node = None
        self.tail = prev
        return node

    def remove(self, value):
        # Remove only the first hit
        prev = None
        cur = self.head
        while cur:
            if cur.value == value:
                if not prev:
                    self.head = self.tail = None
                    return cur
                prev.next_node = cur.next_node
                return cur
            prev = cur
            cur = cur.next_node
        msg = "{0} is not in list".format(value)
        raise ValueError(msg)


def test():
    from simpletest import _assert, _assert_raises
    llist = LinkedList()
    _assert(llist.head, None)
    _assert(llist.tail, None)
    llist.append('a')
    _assert(llist.index('a'), 0)
    _assert(llist.head.value, 'a')
    _assert(llist.tail.value, 'a')
    llist.append('b')
    _assert(llist.index('b'), 1)
    _assert(llist.head.value, 'a')
    _assert(llist.tail.value, 'b')
    llist.append('c')
    _assert(llist.index('c'), 2)
    _assert(llist.head.value, 'a')
    _assert(llist.tail.value, 'c')
    node = llist.pop()
    _assert_raises(ValueError, llist.index, 'c')
    _assert(llist.head.value, 'a')
    _assert(llist.tail.value, 'b')
    _assert(node.value, 'c')
    node = llist.pop()
    _assert(llist.head.value, 'a')
    _assert(llist.tail.value, 'a')
    _assert(node.value, 'b')
    node = llist.pop()
    _assert(llist.head, None)
    _assert(llist.tail, None)
    _assert(node.value, 'a')
    _assert_raises(IndexError, llist.pop)
    llist.append('a')
    llist.append('b')
    llist.append('c')
    for value, expected_value in zip(llist, 'abc'):
        _assert(value, expected_value)
    _assert(llist[0], 'a')
    _assert(llist[1], 'b')
    _assert(llist[2], 'c')
    node = llist.remove('b')
    _assert(node.value, 'b')
    node = llist.remove('c')
    node = llist.remove('a')
    _assert(llist.head, None)
    _assert(llist.tail, None)


if __name__ == '__main__':
    test()
