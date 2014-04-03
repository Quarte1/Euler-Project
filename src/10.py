'''
Created on 2014. 4. 2.

Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million(2,000,000).


Solution:

@author: Ungsik Yun
'''

if __name__ == '__main__':
    from Prime import Prime
    p = Prime()
    l = p.list_under_improved(2000000)
    print sum(l)