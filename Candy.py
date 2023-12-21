"""
Title     : Candy 
Author    : Asmit Singh
Solved On   : 21 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def minCandy(self, N, ratings):
        if N == 1: return 1
        dp = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1

        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1] and dp[i] <= dp[i+1]:
                dp[i] = dp[i+1] + 1

        return sum(dp)

# Time Complexity  : O(n)
# Space Complexity : O(n)