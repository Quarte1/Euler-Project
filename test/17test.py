'''
Created on 2014. 4. 9.

@author: Alice
'''
import unittest
from src.P17 import get_word_from_number, get_alphabet_number


class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual('one', get_word_from_number(1))

    def test10(self):
        self.assertEqual('ten', get_word_from_number(10))

    def test12(self):
        self.assertEqual('twelve', get_word_from_number(12))

    def test42(self):
        self.assertEqual('forty-two', get_word_from_number(42))

    def test342(self):
        self.assertEqual('three hundred and forty-two',
                         get_word_from_number(342))
        self.assertEqual(23, get_alphabet_number(get_word_from_number(342)))

    def test115(self):
        self.assertEqual('one hundred and fifteen',
                         get_word_from_number(115))
        self.assertEqual(20, get_alphabet_number(get_word_from_number(115)))

    def test999(self):
        self.assertEqual('nine hundred and ninety-nine',
                         get_word_from_number(999))

    def test1000(self):
        self.assertEqual('one thousand', get_word_from_number(1000))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
