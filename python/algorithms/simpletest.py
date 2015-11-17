def _assert(actual, expected):
    import inspect
    try:
        print "Test:",
        print inspect.stack()[1][4][0].strip(),
        assert actual == expected, \
                "Expected {0}, got {1}".format(expected, actual)
    except AssertionError as e:
        print "\tFail:", e
    else:
        print "\tPass"
