#!/usr/bin/env python
# −*− coding: UTF−8 −*−
# Topological Sorting

from collections import defaultdict


def topsort(graph):
    if not graph:
        return []
    # 1. Count every node's dependencies
    count = defaultdict(int)
    for node in graph:
        for dependency in graph[node]:
            count[dependency] += 1
    # 2. Find initial nodes - the ones that no dependency points at
    initial_nodes = [node for node in graph if count[node] == 0]
    if graph and not initial_nodes:
        raise Exception("Circular depenency detected")
    # 3. Process each node in the order found in initial_nodes. Populate
    # initial_nodes with processed node's dependencies if these aren't referred
    # in any other node.
    result = []
    while initial_nodes:
        node = initial_nodes.pop()
        result.append(node)
        for dependency in graph[node]:
            count[dependency] -= 1
            if count[dependency] == 0:
                initial_nodes.append(dependency)
    if len(result) != len(graph):
        raise Exception("Circular depenency detected")
    return result[::-1]


def test():
    from simpletest import _assert
    a, b, c, d, e, f = 'abcdef'

    graph = {}
    _assert(topsort(graph), [])

    graph = {
        a: set([]),
    }
    _assert(topsort(graph), [a])

    graph = {
        a: set([d, b]),
        b: set([d, c]),
        c: set([d]),
        d: set([]),
        e: set([d]),
        f: set([d, e]),
    }
    _assert(topsort(graph), [d, c, b, a, e, f])

    graph = {
        a: set([b]),
        b: set([a]),
    }
    try:
        print "Test: Expect exception",
        topsort(graph)
    except Exception as e:
        if str(e) == "Circular depenency detected":
            print "\tPass"
    else:
        print "\tFail: No error found"


if __name__ == '__main__':
    test()
