'''
Title     : Fill the Matrix
Domain    : Mathematical, BFS, Algorithms
Author    : Asmit Singh
Solved On   : 21 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def minIteration(self, N, M, x, y):
        return max(M-y+N-x,y+x-2,y+N-x-1,x+M-y-1)
