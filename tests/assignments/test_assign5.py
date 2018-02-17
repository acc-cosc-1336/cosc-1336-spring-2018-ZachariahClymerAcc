import unittest
from src.assignments.assignment5 import recursive_decimal_binary

#write import for decimal to binary function


class Test_Assign4(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(1,1)

    def test_RDB_w_base_case(self):
        self.assertEqual('00000000', recursive_decimal_binary(0, 7))

    def test_RDB_w_value_65(self):
        self.assertEqual('01000001', recursive_decimal_binary(65, 7))

    #write test cases with arguments 85 and 63 for recursive_decimal_binary function

unittest.main(verbosity=2)
