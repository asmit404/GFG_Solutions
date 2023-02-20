'''
Title     : Count Cyclic Paths
Domain    : Dynamic Programming, Algorithms
Author    : Asmit Singh
Solved On   : 20 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def countPaths (self, N): 
        mod=1000000007
        low,high = 1,0
        tlow,thigh = 1,0
        for i in range(2,N+1):
            high=(3*tlow)%mod
            low=(((2*tlow)%mod)+thigh)%mod
            tlow=low
            thigh=high
        return high
