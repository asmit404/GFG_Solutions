'''
Title     : Unique Paths in a Grid
Domain    : Dynamic Programming, Matrix, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 23 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def uniquePaths(self, n, m, grid):
        if grid[0][0] == 0 or grid[n-1][m-1] == 0: return 0
        vs = [0]*m; vs[0] = 1
        for r in range(n):
            vs[0] = 0 if grid[r][0] == 0 else vs[0] 
            for c in range(1, m):
                if grid[r][c]: vs[c] += vs[c-1]
                else: vs[c] = 0
        return vs[m-1] % (10**9+7)

# There's probably a better way to do this, but i can't be bothered to think about it right now.