"""
Title     : Maximum sum increasing subsequence
Author    : Asmit Singh
Solved On   : 23 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def maxSumIS(self, arr, n):
        n = len(arr)
        dp = arr[:]
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
        return max(dp)

# Time Complexity: O(N^2)
# Space Complexity: O(N)