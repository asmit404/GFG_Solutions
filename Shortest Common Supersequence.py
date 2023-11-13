"""
Title     : Shortest Common Supersequence
Author    : Asmit Singh
Solved On   : 13 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if X[i] == Y[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return (m+n - dp[0][0])

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)