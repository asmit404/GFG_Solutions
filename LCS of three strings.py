"""
Title     : LCS of three strings
Author    : Asmit Singh
Solved On   : 30 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def LCSof3(self, A, B, C, n1, n2, n3):
        dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(2)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    if A[i - 1] == B[j - 1] == C[k - 1]:
                        dp[i % 2][j][k] = dp[(i - 1) % 2][j - 1][k - 1] + 1
                    else:
                        dp[i % 2][j][k] = max(dp[(i - 1) % 2][j][k], dp[i % 2][j - 1][k], dp[i % 2][j][k - 1])
        return dp[n1 % 2][n2][n3]

# Time Complexity: O(n1 * n2 * n3)
# Space Complexity: O(n2 * n3)