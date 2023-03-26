"""
Title     : Frogs and Jumps
Domain    : Arrays, Mathematical, Sieve, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 26 Mar 2023
Solved Using   : Python3
"""

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        unvis = 0
        vis = [False]*(leaves+1)
        for i in range(N):
            curr = frogs[i]
            if curr <= leaves and vis[curr] == False:
                for j in range(curr, leaves+1, curr):
                    vis[j] = True
        for i in range(1, leaves+1):
            if vis[i] == False:
                unvis += 1
        return unvis
