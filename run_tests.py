import unittest

from tests.homework import test_assignment9

suite = unittest.TestLoader().loadTestsFromModule(test_assignment9)
unittest.TextTestRunner(verbosity=2).run(suite)
