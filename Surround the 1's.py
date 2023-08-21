"""
Title     : Surround the 1's
Author    : Asmit Singh
Solved On   : 21 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def Count(self, matrix):
        n, m = len(matrix), len(matrix[0])
        ans = 0
        pool = set()

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and (i, j) not in pool:
                    c = 0
                    for x, y in [i+1, j], [i+1, j+1], [i+1, j-1], [i, j+1], [i-1, j+1], [i, j-1], [i-1, j], [i-1, j-1]:
                        if isValid(x, y) and matrix[x][y] == 0:
                            c += 1
                    if c != 0 and c % 2 == 0:
                        ans += 1
                    pool.add((i, j))
        return ans

# Time Complexity: O(n*m)
# Space Complexity: O(n*m)