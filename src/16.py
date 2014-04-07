'''
Created on 2014. 4. 3.

Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Solution: 1366

@author: Ungsik Yun
'''

i = 2**1000
s = str(i)
sum = 0
for j in s:
    sum += int(j)
print sum
