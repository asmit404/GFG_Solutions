"""
Title     : Grinding Geek
Author    : Asmit Singh
Solved On   : 15 Jan 2024
Solved Using   : Python3
"""

from typing import List
from math import ceil

class Solution:
    def max_courses(self, n: int, total: int, cost: List[int]) -> int:
        dp = [[0]*(total+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for left in range(total+1):
                if cost[i] > left:
                    dp[i][left] = dp[i+1][left]
                else:
                    reduced_cost = ceil(0.1*cost[i])
                    take = 1 + dp[i+1][left-reduced_cost]
                    not_take = dp[i+1][left]
                    dp[i][left] = max(take, not_take)
        return dp[0][total]

# Time Complexity: O(n * total)
# Space Complexity: O(n * total)