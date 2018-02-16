import unittest

from tests.assignment import test_assign5

suite = unittest.TestLoader().loadTestsFromModule(test_assign5) 
unittest.TextTestRunner(verbosity=2).run(suite)
