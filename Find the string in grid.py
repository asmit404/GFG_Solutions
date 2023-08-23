"""
Title     : Find the string in grid
Author    : Asmit Singh
Solved On   : 23 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def searchWord(self, grid, word):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        rows, cols = len(grid), len(grid[0])
        pool = []

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def search(x, y, dx, dy, word):
            for char in word:
                if not is_valid(x, y) or grid[x][y] != char:
                    return False
                x += dx
                y += dy
            return True

        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    if search(i, j, dx, dy, word):
                        pool.append((i, j))
                        break
        return pool

# Time Complexity: O(NML*8)
# Space Complexity: O(K)