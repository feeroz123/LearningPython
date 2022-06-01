import unittest
import sampleTest

class test_sampleTest(unittest.TestCase):

    def test_performTest(self):
        num = 5
        result = sampleTest.squareNum(num)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()