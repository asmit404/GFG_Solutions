"""
Title     : Subarray with given sum
Author    : Asmit Singh
Solved On   : 19 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def subArraySum(self,arr, n, s):
        current_sum, start = arr[0], 0
        for end in range(1, n + 1):
            while current_sum > s and start < end - 1:
                current_sum -= arr[start]
                start += 1
            if current_sum == s:
                return [start + 1, end]
            if end < n:
                current_sum += arr[end]
        return [-1]

# Time Complexity: O(n)
# Space Complexity: O(1)