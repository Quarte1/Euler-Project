'''
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

@author: Ungsik Yun
'''

if __name__ == '__main__':

    sum_of_squares = 0
    square_of_sum = 0

    for i in range(101):
        sum_of_squares += i ** 2
        square_of_sum += i
    square_of_sum = square_of_sum ** 2

    print sum_of_squares
    print square_of_sum
    print square_of_sum - sum_of_squares
