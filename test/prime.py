'''
Created on 2014. 4. 3.

@author: Alice
'''
import unittest
from src.Prime import Prime
from datetime import time

class Test(unittest.TestCase):

    def setUp(self):
        self.p = Prime()
        
    @unittest.skip("test")
    def test_prime(self):
        self.assertEqual(True, self.p.is_prime2(17389))
        self.assertEqual(False, self.p.is_prime2(17388))
        self.assertEqual(False, self.p.is_prime2(17369))
    
    @unittest.skip("test")
    def test_create(self):
        time
        self.p.list_under(5000)
    
    def test_create2(self):
        self.p.list_under_improved(5000)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()