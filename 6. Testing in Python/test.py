import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess('11', 5)
        self.assertFalse(result) #although this works, it does not test for the error which you should test for. 
        #Try to improve this by actually testing for the ValueError it triggers. Hint:
        #self.assertRaises(ValueError)


if __name__ == '__main__':
    unittest.main()
