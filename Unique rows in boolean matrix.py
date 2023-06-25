'''
Title     : Unique rows in boolean matrix
Author    : Asmit Singh
Solved On   : 25 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def uniqueRow(self, row, col, matrix):
        pool = []
        for rw in matrix:
            if rw not in pool:
                pool.append(rw)
        return pool
