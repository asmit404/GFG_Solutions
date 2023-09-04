"""
Title     : Replace Os with Xs
Author    : Asmit Singh
Solved On   : 4 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def fill(self, n, m, mat):
        def floodFill(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] != 'O':
                return
            mat[x][y] = 'T'
            floodFill(x + 1, y)
            floodFill(x - 1, y)
            floodFill(x, y + 1)
            floodFill(x, y - 1)

        for i in range(n):
            floodFill(i, 0)
            floodFill(i, m - 1)

        for i in range(m):
            floodFill(0, i)
            floodFill(n - 1, i)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    mat[i][j] = 'X'
                elif mat[i][j] == 'T':
                    mat[i][j] = 'O'
        return mat

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)