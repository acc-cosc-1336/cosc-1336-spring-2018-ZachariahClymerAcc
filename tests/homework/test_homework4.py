import unittest

#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import sample_function, get_credit_points, valid_letter_grade, get_grade_points, get_grade_point_average

class TestHomework2(unittest.TestCase):

    def test_example(self):
        '''
        This is just an example.
        DON'T CHANGE THIS FUNCTION
        '''
        #assert that 1 equals the return value of the sample_function(1) with argument 1
        self.assertEqual(1, sample_function(1));
    def test_get_credit_points_A(self):
        self.assertEqual(4,get_credit_points('A'))
    def test_get_credit_points_B(self):
        self.assertEqual(3,get_credit_points('B'))
    def test_get_credit_points_C(self):
        self.assertEqual(2,get_credit_points('C'))
    def test_get_credit_points_D(self):
        self.assertEqual(1,get_credit_points('D')) 
    def test_get_credit_points_F(self):
        self.assertEqual(0,get_credit_points('F'))
    def test_get_credit_points_a(self):
        self.assertEqual(4,get_credit_points('a'))
    def test_get_credit_points_b(self):
        self.assertEqual(3,get_credit_points('b'))
    def test_get_credit_points_c(self):
        self.assertEqual(2,get_credit_points('c'))
    def test_get_credit_points_d(self):
        self.assertEqual(1,get_credit_points('d'))
    def test_get_credit_points_f(self):
        self.assertEqual(0,get_credit_points('f'))
        

    def test_valid_letter_grade_B(self):
        self.assertEqual(True,valid_letter_grade('B'))
    def test_valid_letter_grade_Z(self):
        self.assertEqual(False,valid_letter_grade('Z'))

    def test_get_grade_points_3_4(self):
        self.assertEqual(12,get_grade_points(3,4))
    def test_get_grade_point_average(self):
        self.assertEqual(4.0, get_grade_point_average(9.0,36.0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
