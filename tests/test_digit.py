import unittest
from check_digit.check_digit import is_last_digit_even

class TestIsLastDigitEven(unittest.TestCase):
    
    def test_last_digit_even(self):
        self.assertTrue(is_last_digit_even(124))
        self.assertTrue(is_last_digit_even(12))
        self.assertTrue(is_last_digit_even(2))
    
    def test_last_digit_odd(self):
        self.assertFalse(is_last_digit_even(123))
        self.assertFalse(is_last_digit_even(11))
        self.assertFalse(is_last_digit_even(1))

if __name__=="__main__":
    unittest.main()