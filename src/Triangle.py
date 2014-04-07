'''
Created on 2014. 4. 7.

module to find triangle numbers and check

@author: Alice
'''

class Triangle(object):

    def __init__(self):
        self.triangle_number_list = [0]
        
    def get_nth(self,n):
        return (n * (n + 1))/2
    
    def is_triangle(self,i):
        return i in self.triangle_number_list
    
    def get_list_under(self, limit):
        n = 1
        while max(self.triangle_number_list) < limit:
            self.triangle_number_list.append(self.get_nth(n))
            n += 1
        return self.triangle_number_list