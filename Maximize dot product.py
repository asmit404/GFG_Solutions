'''
Title     : Maximize dot product
Author    : Asmit Singh
Solved On   : 7 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def maxDotProduct(self, n, m, a, b):
        pool = [[0]*(m+1) for _ in range(n+1)]
        for j in range(1, m + 1):
            pool[0][j] = float('-inf')
        for i in range(1, n + 1):
            for j in range(1, m+1):
                pool[i][j] = max(pool[i - 1][j], pool[i - 1][j - 1] + a[i - 1] * b[j - 1])
        return pool[n][m]

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)