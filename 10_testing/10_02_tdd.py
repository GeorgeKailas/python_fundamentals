'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
import unittest

class MyFirstTests(unittest.TestCase):
    #does this string equal 'hello world'
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')
    
    def test_less_equal(self):
        self.assertLessEqual(x,y)

if __name__ == '__main__':
    unittest.main()