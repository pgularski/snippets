#!/usr/bin/env python
# −*− coding: UTF−8 −*−


class Test(object):
    def run(self):
        raise NotImplementedError("Implement this!")

    def add(self, test):
        pass


class TestCase(Test):
    def run(self):
        print "Running test: %s" % self


class TestSuite(Test):
    def __init__(self):
        self.tests = []

    def run(self):
        for test in self.tests:
            test.run()

    def add(self, test):
        self.tests.append(test)


def test():
    test01 = TestCase()
    test02 = TestCase()
    test03 = TestCase()
    testsuite01 = TestSuite()
    testsuite02 = TestSuite()
    testsuite03 = TestSuite()

    testsuite01.add(test01)
    testsuite01.add(test02)
    testsuite02.add(test03)
    testsuite03.add(testsuite01)
    testsuite03.add(testsuite02)
    testsuite03.add(test01)

    testsuite03.run()


if __name__ == '__main__':
    test()
