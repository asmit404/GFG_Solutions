"""
Title     : Anti Diagonal Traversal of Matrix
Author    : Asmit Singh
Solved On   : 27 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def antiDiagonalPattern(self, matrix):
        res = []
        n = len(matrix)
        for sum in range(2 * n - 1):
            if sum < n:
                i = 0
                j = sum
            else:
                i = sum - n + 1
                j = n - 1
            while i < n and j >= 0:
                res.append(matrix[i][j])
                i += 1
                j -= 1
        return res

# Time Complexity  : O(n ^ 2)
# Space Complexity : O(n ^ 2)