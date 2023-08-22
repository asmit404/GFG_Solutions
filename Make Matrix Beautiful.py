"""
Title     : Make Matrix Beautiful 
Author    : Asmit Singh
Solved On   : 22 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def findMinOpeartion(self, matrix, n):
        maxr, maxc = 0, 0
        for i in range(n):
            row_sum, col_sum = 0, 0
            for j in range(n):
                row_sum += matrix[i][j]
                col_sum += matrix[j][i]
            maxr, maxc = max(maxr, row_sum), max(maxc, col_sum)
        return max(maxr, maxc)*n - sum(sum(row) for row in matrix)

# Time Complexity: O(n^2)
# Space Complexity: O(1)