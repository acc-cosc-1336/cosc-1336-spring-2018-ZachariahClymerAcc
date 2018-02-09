import unittest

from tests.assignment import test_assign4

suite = unittest.TestLoader().loadTestsFromModule(test_assign4)
unittest.TextTestRunner(verbosity=2).run(suite)
