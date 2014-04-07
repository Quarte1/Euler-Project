'''
Created on 2014. 4. 7.

@author: Alice
'''
import unittest
from src.Triangle import Triangle

class Test(unittest.TestCase):


    def setUp(self):
        self.t = Triangle()
    
    def test_get(self):
        self.assertEqual(28, self.t.get_nth(7))
        
    def test_list(self):
        l = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        self.assertEqual(l, self.t.get_list_under(120))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()