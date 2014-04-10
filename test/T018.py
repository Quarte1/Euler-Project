'''
Created on 2014. 4. 10.

@author: Alice
'''
import unittest


from src.P018 import find_maximum_path


class Test(unittest.TestCase):

    def test1(self):
        l = [
             [3],
             [7, 4],
             [2, 4, 6],
             [8, 5, 9, 3]
             ]
        self.assertEqual(23, find_maximum_path(l))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
