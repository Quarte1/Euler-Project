'''

Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the result of the even-valued terms.

'''


def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":

    a = 0
    b = 1
    f = fib()
    cnt = 0
    result = 0
    for i in f:
        if i < 4000000 and i % 2 == 0:
            print i
            result += i
        elif i > 4000000:
            break

        cnt += 1

    print "!"
    print "result: ", result