"""
Title     : Letters Collection
Author    : Asmit Singh
Solved On   : 06 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def hop(self, row, col, n, N, M, matrix):
        total = 0
        for i in range(max(0, row-n), min(N, row+n+1)):
            for j in range(max(0, col-n), min(M, col+n+1)):
                if i == row-n or i == row+n or j == col-n or j == col+n:
                    total += matrix[i][j]
        return total

    def matrixSum(self, n, m, mat, q, queries):
        return [self.hop(query[1], query[2], query[0], n, m, mat) for query in queries]

# Time Complexity: O(n * m * q)
# Space Complexity: O(1)