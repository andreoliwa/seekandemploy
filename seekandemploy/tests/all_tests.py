#!/usr/bin/python2.7 -tt
# coding=utf-8

"""
Test suite for all tests
"""

import unittest
import glob
import os
import sys


def build_test_suite():
    """
    Build a testsuite for test_*.
    """

    suite = unittest.TestSuite()

    file_mask = os.path.join(sys.path[0], 'test_*.py')
    for test_case in glob.glob(file_mask):
        mod_name = os.path.splitext(test_case)[0]
        mod_name = os.path.basename(mod_name)
        module = __import__(mod_name, {}, {}, ['1'])
        suite.addTest(unittest.TestLoader().loadTestsFromModule(module))

    return suite


def main():
    """
    Program entry-point.
    """

    print '===================='
    print ' Running all tests'
    print '===================='

    suite = build_test_suite()
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()
