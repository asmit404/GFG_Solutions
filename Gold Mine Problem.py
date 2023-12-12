"""
Title     : Gold Mine Problem
Author    : Asmit Singh
Solved On   : 12 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def maxGold(self, n, m, M):
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]

        for j in range(m - 2, -1, -1):
            for i in range(n):
                up_right = dp[i - 1][j + 1] if i > 0 else 0
                right = dp[i][j + 1]
                down_right = dp[i + 1][j + 1] if i < n - 1 else 0
                dp[i][j] = M[i][j] + max(up_right, right, down_right)

        return max(dp[i][0] for i in range(n))

# Time Complexity: O(nm)
# Space Complexity: O(nm)