"""
Title     : Number Of Enclaves
Author    : Asmit Singh
Solved On   : 29 Sept 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = []
        l = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and grid[i][j] == 1:
                    l[i][j] = 1
                    queue.append((i, j))

        while queue:
            row, col = queue.pop(0)
            for i, j in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= i < n and 0 <= j < m and l[i][j] == 0 and grid[i][j] == 1:
                    queue.append((i, j))
                    l[i][j] = 1

        return sum(grid[i][j] == 1 and l[i][j] == 0 for i in range(n) for j in range(m))

# Time Complexity: O(n*m)
# Space Complexity: O(n*m)