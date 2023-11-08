"""
Title     : Print Matrix in snake Pattern
Author    : Asmit Singh
Solved On   : 08 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def snakePattern(self, matrix):
        path = []
        for i, row in enumerate(matrix):
            if i & 1:
                path.extend(reversed(row))
            else:
                path.extend(row)
        return path

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)