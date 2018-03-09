import unittest
from src.midterm.exam import get_miles_per_hour, get_bonus_pay_amount, get_bonus_pay_amount, get_list_min_max, get_list_min_max_file
#write import statements for exam functions

class Test_Midterm(unittest.TestCase):

    def test_get_miles_per_hour(self):
        '''
        5 points
        Test with arguments kilometers 32 and minutes 60 return value should be 19.883872
        '''
        self.assertEqual(19.883872, (32 ,60))


    def test_get_bonus_pay_amount_w_good_value (self):
        '''
        5 points
        Test with value 1000 return value should be 70
        '''
        self.assertEqual(70 , sales(1000))


    def test_get_bonus_pay_amount_w_bad_value(self):
        '''
        5 points
        Test with -5 return value should be 'Invalid arguments'
        '''
        self.assertEqual('Invalid input', sales(-5))


    def test_reverse_string(self):
        '''
        5 points
        Test with value My String Data return value should be ataD gnirtS yM
        '''
        self.assertEqual('ataD gnirtS yM', string1('My String Data'))


    def test_get_list_min_max(self):
        '''
        5 points
        Test with ['joe', 10, 15, 20, 30, 40]    Returns:    [10, 40]
        '''
        self.assertEqual('10, 40', list1('joe', 10, 15, 20, 30, 40))


    def test_get_list_min_max_file(self):
        '''
        5 points
        Test with quiz.data file the return value should be [2,89]
        '''
        self.assertEqual([2,89], quiz.data)


unittest.main(verbosity = 2)
    
