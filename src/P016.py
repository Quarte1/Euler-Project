'''
Created on 2014. 4. 3.

Power digit result
Problem 16
215 = 32768 and the result of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the result of the digits of the number 2^1000?

Solution: 1366

@author: Ungsik Yun
'''
if __name__ == '__main__':
    i = 2 ** 1000
    s = str(i)
    result = 0
    for j in s:
        result += int(j)
    print result
