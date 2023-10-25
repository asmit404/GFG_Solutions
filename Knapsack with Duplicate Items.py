"""
Title     : KnapSack with Duplicate Items
Author    : Asmit Singh
Solved On   : 25 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def knapSack(self, N, W, val, wt):
        dp = [0] * (W + 1)
        for j in range(N):
            for i in range(wt[j], W + 1):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
        return dp[W]

# Nice Question.
# Time Complexity: O(N*W)
# Space Complexity: O(W)