'''
Created on 2014. 4. 8.

Lattice paths
Problem 15
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20*20 grid?


@author: Alice
'''

if __name__ == '__main__':
    n, m = 20, 20
    matrix = [[1 for i in xrange(n+1)] for j in xrange(m+1)]

    #calculate
    for line in xrange(1, m+1):
        for i in xrange(1, n+1):
            matrix[line][i] = matrix[line][i-1] + matrix[line-1][i]
    
    for i in matrix:
        print i
