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
            if self.is_prime(i):
                if i not in self.prime_list :
                    self.prime_list.append(i)
        result = []
        for j in self.prime_list:
            if j < limit:
                result.append(j)
            else:
                break
        return result
        
        
    def is_prime(self, i):
        if i == 2:
            return True 
        else :
            for prime in self.prime_list:
                if i % prime == 0 :
                    return False
        return True

        
    def is_prime2(self, target):
        if target == 2:
            return True
        
        for i in range(3, target
                       , 2):
            if target % i == 0:
                return False
        return True
    
    
    def biggest_under(self, limit):
        primes = self.list_under(limit)
        return primes[-1]
    
    
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
    print prime.is_prime2(3)
    print prime.is_prime2(31)
    print prime.is_prime2(30)
    print prime.is_prime2(19)
