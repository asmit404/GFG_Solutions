'''
Title     : Maximum Triplet Product
Domain    : Arrays, Mathematical, Data Structures, Algorithms 
Author    : Asmit Singh
Solved On   : 10 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def maxTripletProduct (self, a,  n): 
        a.sort()
        return max(a[0]*a[1]*a[-1],a[-1]*a[-2]*a[-3])
