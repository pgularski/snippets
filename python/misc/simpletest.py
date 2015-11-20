def _assert(actual, expected):
    import inspect
    try:
        line = inspect.stack()[1][2]
        print "Test:",
        print inspect.stack()[1][4][0].strip(),
        assert actual == expected, \
            "Line {0}: Expected {1}, got {2}".format(line, expected, actual)
    except AssertionError as e:
        print "\tFail:", e
    else:
        print "\tPass"


def _assert_raises(exception, callback, *args, **kwargs):
    import inspect
    line = inspect.stack()[1][2]
    try:
        print "Test:",
        print inspect.stack()[1][4][0].strip(),
        callback(*args, **kwargs)
    except exception:
        print "\tPass"
    else:
        print "\tFail: Line {0}: Exception not raised: {0}".format(
                line, exception.__name__)
