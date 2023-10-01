"""
Title     : Boundary traversal of matrix
Author    : Asmit Singh
Solved On   : 1 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def BoundaryTraversal(self, mat, n, m):
        pool = []
        for i in range(m):
            pool.append(mat[0][i])
        for i in range(1, n-1):
            pool.append(mat[i][m-1])
        for i in range(m-1, -1, -1):
            if n > 1:
                pool.append(mat[n-1][i])
        for i in range(n-2, 0, -1):
            if m > 1:
                pool.append(mat[i][0])
        return pool

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)