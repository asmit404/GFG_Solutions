"""
Title     : Determinant of a Matrix
Author    : Asmit Singh
Solved On   : 25 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def determinantOfMatrix(self, matrix, n):
        if n == 1: return matrix[0][0]
        if n == 2: return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        deter = 0
        for i in range(n):
            minor = [row[:i] + row[i+1:] for row in matrix[1:]]
            cofac = matrix[0][i]*((-1) ** i)
            deter += cofac * self.determinantOfMatrix(minor, n-1)
        return deter

# Time Complexity  : O(n!)
# Space Complexity : O(n)