'''
Created on 2014. 3. 31.

Find prime numbers

@author: Ungsik Yun
'''



def prime_list_under(limit):
    
    prime_list = [2,3]
    for i in range(3, limit+1):
        if is_prime(prime_list, i):
            prime_list.append(i)
    
    return prime_list
    
    
def is_prime(prime_list, i):
    if i == 2:
        return True 
    elif i % 2 == 0:
        return False
    else :
        for prime in prime_list:
            if i % prime == 0 :
                return False
    return True

def prime_biggest_under(limit):
    primes = prime_list_under(limit)
    return primes[-1]

if __name__ == "__main__":
    prime_list_under(100)
    prime_biggest_under(100)