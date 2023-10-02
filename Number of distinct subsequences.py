"""
Title     : Number of distinct subsequences
Author    : Asmit Singh
Solved On   : 2 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def distinctSubsequences(self, S):
        mod = 10**9 + 7
        n = len(S)
        dp = [1] + [0] * n
        last = {}

        for i, ch in enumerate(S, 1):
            dp[i] = (2 * dp[i - 1]) % mod

            if ch in last:
                dp[i] = (dp[i] - dp[last[ch] - 1] + mod) % mod

            last[ch] = i

        return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)