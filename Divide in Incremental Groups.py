"""
Title     : Divide in Incremental Groups
Domain    : Dynamic Programming, Mathematical, Data Structures
Author    : Asmit Singh
Solved On   : 27 Mar 2023
Solved Using   : Python3
"""

class Solution:
    def countWaystoDivide(self, N, K):
        dp = [[0] * (K+1) for _ in range(N+1)]
        for i in range(1, N+1):
            dp[i][1] = 1
        for i in range(2, N+1):
            for j in range(2, min(i+1, K+1)):
                dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
        return dp[N][K]
