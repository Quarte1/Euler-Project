'''
Created on 2014. 3. 31.

Problem 3
The Prime factors of 13195 are 5, 7, 13 and 29.

What is the largest Prime factor of the number 600851475143 ?


Solution: just brute force. select 10000 prime number from 2, than try divide. it's so silly way i think...

@author: Ungsik Yun
'''

import Prime
def get_lagerst_prime_factor(target):
    
    factors =[]
    p = Prime.Prime()
    primes_temp = p.list_under(10000)
#     primes = list_under(target)
    
    for prime in primes_temp :
        if target % prime == 0 :
            target = target / prime
            factors.append(prime)
    
    return factors

if __name__ == "__main__":
#     print get_lagerst_prime_factor(13195)
    print get_lagerst_prime_factor(600851475143)