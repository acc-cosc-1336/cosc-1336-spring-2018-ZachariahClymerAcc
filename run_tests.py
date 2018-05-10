import unittest

from tests.assignment import test_assignment11

suite = unittest.TestLoader().loadTestsFromModule(test_assignment11)
unittest.TextTestRunner(verbosity=2).run(suite)
