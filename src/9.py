'''
Created on 2014. 4. 2.

Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solution:
Spread equations, get next equation: 500000 == 1000*a + 1000*b - a*b
I can get a & b from below iteration. than can calculate c.

@author: Alice
'''



if __name__ == '__main__':
    from math import sqrt
    
    a,b = 0,0
    target = 500000
    has_found = False
    while b < 1000 and not has_found:
        a = 1
        b += 1
        while a < b and not has_found:
            a += 1
            if target == 1000*a + 1000*b - a*b:
                print a,b
                has_found = True
    c_square = a**2 + b**2
    c = sqrt(c_square)
    print a,b,c,a+b+c, a*b*c