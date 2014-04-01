'''
Created on 2014. 3. 31.

Find prime numbers

@author: Ungsik Yun
'''


class Prime(object):

    def __init__(self):
        self.prime_list = [2,3]

    def list_under(self, limit):
    
        for i in range(3, limit+1, 2):
            if self.is_prime(self.prime_list, i):
                if i not in self.prime_list :
                    self.prime_list.append(i)
    
        return self.prime_list
        
        
    def is_prime(self, prime_list, i):
        if i == 2:
            return True 
        elif i % 2 == 0:
            return False
        else :
            for prime in prime_list:
                if i % prime == 0 :
                    return False
        return True
    
    
    def biggest_under(self, limit):
        primes = self.list_under(limit)
        return primes[-1]
    
    
    def get_by(self, number):
        
     
        return self.prime_list

if __name__ == "__main__":
    prime = Prime()
    print prime.list_under(100000)
#     biggest_under(100)