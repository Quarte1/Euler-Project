'''
Created on 2014. 3. 31.

Find prime numbers

@author: Ungsik Yun
'''
from math import sqrt, floor
import datetime

class Prime(object):

    def __init__(self):
        self.prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def list_under(self, limit):
        for i in xrange(101, limit+1, 2):
            if self.is_prime(i):
                if i not in self.prime_list :
                    self.prime_list.append(i)
        result = []
        for i1 in self.prime_list:
            if i1 < limit:
                result.append(i1)
            else:
                break
        return result
    
    def list_under_improved(self, limit):
        for i in xrange(102, limit+1, 6):
            i1, i2 = i - 1, i + 1
            if self.is_prime2(i1):
                if i1 not in self.prime_list :
                    self.prime_list.append(i1)
            if self.is_prime2(i2):
                if i2 not in self.prime_list :
                    self.prime_list.append(i2)
        return self.prime_list
        
        
    def is_prime(self, i):
        if i == 2:
            return True 
        else :
            for prime in self.prime_list:
                if i % prime == 0 :
                    return False
        return True

        
    def is_prime2(self, target):
        if target in self.prime_list:
            return True
        else:
            divider =  int(sqrt(target)) + 1
            for i in xrange(2, divider):
                if target % i == 0:
                    return False
            return True
    
    
    def get_by(self, stop):
        target = self.prime_list[-1]
        while len(self.prime_list) < stop :
            if self.is_prime(target) :
                self.prime_list.append(target)
            else:
                target += 1
        
        return self.prime_list[0:stop]
    
    
    def next_prime(self, ):
        pass
    
    
if __name__ == "__main__":
    prime = Prime()
    a = datetime.datetime.now()
    print prime.list_under_improved(100000)
    b = datetime.datetime.now()
    print b - a
    

