"""
Title     : Max Sum Subarray of size K
Author    : Asmit Singh
Solved On   : 11 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def maximumSumSubarray (self, K, Arr, N):
        windowSum = sum(Arr[:K])
        maxSum = windowSum
        windowStart = 0
        for windowEnd in range(K, N):
            windowSum = windowSum - Arr[windowStart] + Arr[windowEnd]
            maxSum = max(windowSum, maxSum)
            windowStart += 1
        return maxSum

# Time Complexity  : O(n)
# Space Complexity : O(1)