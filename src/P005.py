'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

@author: Ungsik Yun
'''

if __name__ == '__main__':
    number = 0
    continue_flag = 1
    # l = [2,3,5,7,11,13,17,19]
    l = range(1, 21)

    while True:
        continue_flag = 0
        number += 20
        for i in l:
            if number % i != 0:
                continue_flag += 1
        if number % 100000 == 0:
                    print "number: %d\t continue_flag: %d" % (number, continue_flag)
        if continue_flag == 0:
            print "Number is ", number
