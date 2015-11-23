#!/usr/bin/env python
# −*− coding: UTF−8 −*−

from linked_list import LinkedList


def add(list_a, list_b):
    list_c = LinkedList([0])

    node_a = list_a.head
    node_b = list_b.head
    node_c = list_c.head

    carry = 0
    while node_a or node_b:
        a = node_a.value if node_a else 0
        b = node_b.value if node_b else 0

        result = a + b + carry
        carry, result = divmod(result, 10)
        node_c.value = result
        if carry:
            list_c.append(carry)

        node_a = node_a.next_node if node_a else None
        node_b = node_b.next_node if node_b else None
        node_c = node_c.next_node

    return list_c


def test():
    from simpletest import _assert
    _assert(add(LinkedList([]), LinkedList([])), LinkedList([0]))
    _assert(add(LinkedList([1]), LinkedList([])), LinkedList([1]))
    _assert(add(LinkedList([0]), LinkedList([1])), LinkedList([1]))
    _assert(add(LinkedList([1]), LinkedList([1])), LinkedList([2]))
    _assert(add(LinkedList([9]), LinkedList([1])), LinkedList([0, 1]))
    _assert(add(LinkedList([9, 9]), LinkedList([3, 8, 9])),
            LinkedList([2, 8, 0, 1]))


if __name__ == '__main__':
    test()
