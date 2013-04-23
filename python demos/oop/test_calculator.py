# test_calculator.py

from calculator import *
import unittest

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(6,7), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)

    def test_divide(self):
        self.assertEqual(divide(9,3), 3)

#main
if __name__ == "__main__":
    unittest.main()

##.... -> each dot means pass
##----------------------------------------------------------------------
##Ran 4 tests in 0.080s
##
##OK
##Traceback (most recent call last):
##  File "F:/ngyuansiang/Demos/python demos/oop/test_calculator.py", line 21, in <module>
##    unittest.main()
##  File "C:\Python33\lib\unittest\main.py", line 125, in __init__
##    self.runTests()
##  File "C:\Python33\lib\unittest\main.py", line 263, in runTests
##    sys.exit(not self.result.wasSuccessful())
##SystemExit: False
