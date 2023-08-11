"""
Title     : Coin Change
Author    : Asmit Singh
Solved On   : 11 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def count(self, coins, N, Sum):
        dp = [0]*(Sum+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, Sum+1):
                dp[i] += dp[i-coin]
        return dp[Sum]

# Time Complexity : O(N*Sum)
# Space Complexity : O(Sum)