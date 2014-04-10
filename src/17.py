'''
Created on 2014. 4. 9.

Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.


@author: Alice
'''


def get_word_from_number(n):

    words = {
             1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine',
             10: 'ten',
             11: 'eleven',
             12: 'twelve',
             13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen',
             16: 'sixteen',
             17: 'seventeen',
             18: 'eighteen',
             19: 'nineteen',
             20: 'twenty',
             30: 'thirty',
             40: 'forty',
             50: 'fifty',
             60: 'sixty',
             70: 'seventy',
             80: 'eighty',
             90: 'ninety',
             100: 'hundred',
             1000: 'thousand',
             }
    stringed = ''
    for i in xrange(len(str(n)), 0, -1):
        divisor = int('1' + '0' * (i - 1))

        if n > 0 and n < 20:
            stringed += words[n]
            break
        elif n > 19 and n < 100:
            ten = int(str(n)[0]) * 10
            stringed += words[ten]
            if n % 10 > 0:
                stringed += '-'
                stringed += words[n % 10]
            break
        elif n >= 100:
            stringed += words[n / divisor]
            if i > 1:
                stringed += ' ' + words[divisor]
                if n % divisor > 0:
                    stringed += ' and '
#                     if n % divisor > 10:
#                         stringed += 'and '
        n = n % divisor

    return stringed


def get_alphabet_number(s):
    return len(s.replace(' ', '').replace('-', ''))


def get_alphaber_sum_under(target):
    result = 0
    for i in xrange(1, target + 1):
        print "%4d: %2d, %s" % (i,
                                get_alphabet_number(get_word_from_number(i)),
                                get_word_from_number(i))
        result += get_alphabet_number(get_word_from_number(i))
    return result

if __name__ == '__main__':
    print get_alphaber_sum_under(1000)