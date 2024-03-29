'''
Title     : Rod Cutting
Author    : Asmit Singh
Solved On   : 12 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            for j in range(i):
                dp[i] = max(dp[i], price[j] + dp[i - j - 1])
        return dp[n]
