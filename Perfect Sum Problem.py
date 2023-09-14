"""
Title     : Perfect Sum Problem
Author    : Asmit Singh
Solved On   : 14 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def perfectSum(self, arr, n, sum):
        MOD = 10**9 + 7

        dp = [0] * (sum + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(sum, arr[i]-1, -1):
                dp[j] = (dp[j] + dp[j-arr[i]]) % MOD

        return dp[sum]

# Time Complexity: O(n * sum)
# Space Complexity: O(sum)