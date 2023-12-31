"""
Title     : New Year Resolution
Author    : Asmit Singh
Solved On   : 31 Dec 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def isPossible(self, n: int, arr: List[int]) -> bool:
        dp = [[0]*(n+1) for _ in range(2025)]
        for i in range(n+1):
            dp[0][i] = True
        for s in range(1, 2025):
            for i in range(n):
                dp[s][i+1] = dp[s][i]
                if s >= arr[i]:
                    dp[s][i+1] = dp[s][i+1] or dp[s-arr[i]][i]
            if dp[s][n] and (s % 20 == 0 or s % 24 == 0 or s == 2024):
                return True
        return False

# Closing 2023 with a 212 day streak.
# Time Complexity  : O(n * S)
# Space Complexity : O(n * S)