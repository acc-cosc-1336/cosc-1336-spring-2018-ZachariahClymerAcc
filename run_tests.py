import unittest

from tests.assignment import test_assignment10

suite = unittest.TestLoader().loadTestsFromModule(test_assignment10)
unittest.TextTestRunner(verbosity=2).run(suite)
