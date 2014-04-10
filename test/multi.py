'''
Created on 2014. 4. 7.

@author: Alice
'''

from multiprocessing import Process

def f(name):
    print 'hello', name

if __name__ == '__main__':
    p1 = Process(target=f, args=('bob',))
    p2 = Process(target=f, args=('sally',))
    p3 = Process(target=f, args=('pap',))
    p1.start()
    p2.start()
    p3.start()
