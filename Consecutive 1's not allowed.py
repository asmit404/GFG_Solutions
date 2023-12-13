"""
Title     : Consecutive 1's not allowed
Author    : Asmit Singh
Solved On   : 13 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def countStrings(self, n):
        MOD = 1000000007
        dp = [0, 2, 3] + [0]*(n-2)
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        return dp[n]

# Time Complexity  : O(n)
# Space Complexity : O(n)