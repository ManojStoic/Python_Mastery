import unittest
import Python_Scripts_2022_Udemy

class TestMain(unittest.TestCase):

    # useful method that runs before every test case method
    def setUp(self) -> None:
        print("About to test a function")

    def test_sum(self):
        """Test case to test sum of two integers method"""
        x,y = 10,20
        result = Python_Scripts_2022_Udemy.sum(x,y)
        self.assertEqual(result,x+y)

    def test_sub(self):
        """Test case to test diff of two integers method"""
        x,y = 10,20
        result = Python_Scripts_2022_Udemy.sub(x,y)
        self.assertEqual(result,y-x)

    # Negative testing scenarios

    def test_ValueErrors(self):
        """Test case to test Value type errors"""
        x,y = "Manoj",20
        result = Python_Scripts_2022_Udemy.sum(x,y)
        self.assertIsInstance(result,ValueError)

    def test_NoneTypeErrors(self):
        """Test case to test None type errors"""
        x,y = None,20
        result = Python_Scripts_2022_Udemy.sum(x,y)
        self.assertEqual(result,"Please return a number")

    def test_NullErrors(self):
        """Test case to test Null type errors"""
        x,y = "",20
        result = Python_Scripts_2022_Udemy.sum(x,y)
        self.assertEqual(result,"Please return a number")

    # useful method to cleanup the test cases
    def tearDown(self) -> None:
        print("Cleaning up the function")

if __name__ == '__main__':
    unittest.main()

# use 'python -m unittest' command to run all test modules without mentioning the script
# use 'python -m unittest -v' command to run all test modules without mentioning the script and list the docstrings