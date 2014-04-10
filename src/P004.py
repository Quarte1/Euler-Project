'''
Created on 2014. 4. 1.

Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Solution: 906609

@author: Ungsik Yun
'''


def is_palindrome(i):
    stringed = str(i)
    for i in range(len(stringed) / 2):
        if stringed[i] != stringed[-(i + 1)]:
            return False
            break
    return True


def is_palindrome_improved(i):
    return str(i) == str(i)[::-1]


def get_largest_2_3digit_multifled_pelindrome():
    pelindrome_list = []

    i, j = 999, 999
    while i > 100:
        j = 999
        while j > 100:
#             print i,j
            if is_palindrome_improved(i * j):
                pelindrome_list.append(i * j)
            j -= 1
        i -= 1
    return max(pelindrome_list)

if __name__ == '__main__':
    print get_largest_2_3digit_multifled_pelindrome()
