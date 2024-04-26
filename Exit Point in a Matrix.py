'''
Title     : Exit Point in a Matrix
Author    : Asmit Singh
Solved On   : 26 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def FindExitPoint(self, n, m, mat):
        x = y = direction = 0
        pool = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while 0 <= x < n and 0 <= y < m:
            if mat[x][y] == 1:
                direction = (direction + 1) % 4
                mat[x][y] = 0
            dx, dy = pool[direction]
            x += dx
            y += dy
        return max(min(x, n-1), 0), max(min(y, m-1), 0)

# Time Complexity: O(n * m)
# Space Complexity: O(1)