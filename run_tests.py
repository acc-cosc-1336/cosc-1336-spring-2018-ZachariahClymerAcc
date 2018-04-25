import unittest

from tests.assignment import test_assignmentk7
#import test_homework7

suite = unittest.TestLoader().loadTestsFromModule(test_assignment7)
unittest.TextTestRunner(verbosity=2).run(suite)
