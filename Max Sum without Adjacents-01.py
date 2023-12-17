"""
Title     : Max Sum without Adjacents
Author    : Asmit Singh
Solved On   : 17 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def findMaxSum(self, arr, n):
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])

        dp = [-1 for _ in range(n)]
        dp[0], dp[1] = arr[0], max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], arr[i]+dp[i-2])

        return dp[-1]

# First Time seeing a question repeated, also seen on 4th Feb 2023
# Time Complexity  : O(n)
# Space Complexity : O(n)