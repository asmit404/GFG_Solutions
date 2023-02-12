'''
Title     : Minimum Days
Domain    : Linked List, Mathematical, Prime Number, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 12 Feb 2023
Solved Using   : Python3
'''

from typing import Optional
from math import sqrt

class Solution:
    def isPrime(self,x):
        if x<2:
            return False
        if x==2 or x==3:
            return True
        if x%2==0 or x%3==0:
            return False
        for i in range(5,int(sqrt(x))+1,6):
            if (x%i==0) or (x%(i+2)==0):
                return False
        return True
    
    def makePrime(self,x):
        if self.isPrime(x):
            return x
        if x == 1: return 2
        else:
            for i in range(1,x):
                if self.isPrime(x-i):
                    return (x-i)
                elif self.isPrime(x+i):
                    return (x+i)
        return x
        
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        temp = head
        while temp!=None:
            temp.data = self.makePrime(temp.data)
            temp = temp.next
        return head
