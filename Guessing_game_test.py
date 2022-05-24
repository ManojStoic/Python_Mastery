"""
source: Python_Scripts\Guessing_game.py

"""

import unittest
from Guessing_game import guess_number

class TestMain(unittest.TestCase):

    def test_guess_num(self):
        for i in range(1,6):
            result = guess_number(i)
            self.assertIn(result,["Hurrah! You guessed it right!","Close but wrong! Try again"])

    def test_guess_num_outofrange(self):
        input_num = 10
        result = guess_number(input_num)
        self.assertEqual(result,"Number invalid - Enter a valid number!")

    def test_guess_num_err_Value(self):
        input_num = None
        result = guess_number(input_num)
        self.assertEqual(result,"Number invalid - Enter a valid number!")
    
    def test_guess_num_err_Type(self):
        input_num = ""
        result = guess_number(input_num)
        self.assertEqual(result,"Number invalid - Enter a valid number!")

if __name__=="__main__":
    unittest.main()