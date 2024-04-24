'''
Title     : Paths to reach origin
Author    : Asmit Singh
Solved On   : 24 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def ways(self, n, m):
        MOD = 1000000007
        pool = [[None]*(m + 1) for _ in range(n+1)]
        for i in range(m + 1):
            pool[0][i] = 1
        for i in range(n + 1):
            pool[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                pool[i][j] = pool[i - 1][j] + pool[i][j - 1]
        return pool[n][m] % MOD

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)