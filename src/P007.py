'''
Created on 2014. 4. 2.
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
@author: Alice
'''

import Prime

if __name__ == '__main__':
    p = Prime.Prime()
    l = p.get_by(10001)
    print l[-1]
