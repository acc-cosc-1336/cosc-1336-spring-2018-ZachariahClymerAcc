import unittest

from tests.homework import test_homework 11

suite = unittest.TestLoader().loadTestsFromModule(test_homework 11)
unittest.TextTestRunner(verbosity=2).run(suite)
