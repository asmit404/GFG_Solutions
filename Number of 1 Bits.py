'''
Title     : Number of 1 Bits
Author    : Asmit Singh
Solved On   : 1 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def setBits(self, N):
        count = 0
        while (N > 0):
            count += N % 2
            N = N//2
        return count
