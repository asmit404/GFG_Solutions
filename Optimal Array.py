'''
Title     : Optimal Array
Domain    : Arrays, Sorting, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 28 Feb 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        z=[]
        c=0
        for i in range(n):
            c=c+a[i]-a[i//2]
            z.append(c)
        return z
