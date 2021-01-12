'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
tests should pass. Also include a test that does not pass.

NOTE: You can write both the code as well as the tests for it in this single file.
However, feel free to adhere to best practices and separate your tests and the functions you are testing
into different files. Note that you will run into an error when attempting to import this file,
because Python modules can't begin with a number.

'''
import unittest

class TestSubtractDivide(unittest.TestCase):
    def test_equal(self):
        # result = subtract_divide(7,5,10)
        self.assertEquals(subtract_divide(6,1,2), -6)
    def test_divzero(self):
        with self.assertRaises(ZeroDivisionError):
            subtract_divide(4,5,4)
    def test_greater(self):
        self.assertGreater(subtract_divide(6,1,2),-10)


def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        print(f"this won't work, {x} - {y} is 0 or lower.")
        raise ZeroDivisionError

if __name__ == '__main__':
    unittest.main()
