"""
Title     : Sum of upper and lower triangles
Author    : Asmit Singh
Solved On   : 07 Nov 2023
Solved Using   : Python3
"""
 
class Solution:
    def sumTriangles(self, matrix, n):
        x = y = z = 0
        for i in range(n):
            for j in range(i+1, n):
                x += matrix[i][j]
        for i in range(n):
            y += matrix[i][i]
        for i in range(1, n):
            for j in range(i):
                z += matrix[i][j]
        return [x+y, y+z]

# Time Complexity: O(n^2)
# Space Complexity: O(1)