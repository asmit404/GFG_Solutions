"""
Title     : Make Array Elements Equal
Domain    : Arrays, Mathematical, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 01 Apr 2023
Solved Using   : Python3
"""

class Solution:
    def minOperations(self, N):
        return (N//2) * (N-(N//2))
