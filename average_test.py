import unittest
from average import findAverage   # assume function is in average.py


class TestFindAverage(unittest.TestCase):

    # Test Case 1: normal values within range
    def testNormalValues(self):
        result = findAverage([2,4,6], 0, 10)
        self.assertEqual(result, 4.0)

    # Test Case 2: some values outside range
    def testValuesOutsideRange(self):
        result = findAverage([-5, 3, 12, 5], 0, 10)
        self.assertEqual(result, 4.0)

    # Test Case 3: no valid values
    def testNoValidValues(self):
        result = findAverage([-5, 20, 30], 0, 10)
        self.assertEqual(result, -999)

    # Test Case 4: sentinel value stops loop
    def testSentinelValue(self):
        result = findAverage([4,5,-999,8], 0, 10)
        self.assertEqual(result, 4.5)

    # Test Case 5: input limit (max 10 inputs counted)
    def testMaxInputLimit(self):
        result = findAverage([1,2,3,4,5,6,7,8,9,10,11], 0, 10)
        self.assertEqual(result, 5.5)

    # Test Case 6: empty list
    def testEmptyList(self):
        result = findAverage([], 0, 10)
        self.assertEqual(result, -999)


if __name__ == "__main__":
    unittest.main()