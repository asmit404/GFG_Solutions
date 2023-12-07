"""
Title     : Number of subarrays with maximum values in given range
Author    : Asmit Singh
Solved On   : 07 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def countSubarrays(self, nums, n, left, right): 
        start = end = res = window_count = 0
        while end < len(nums):
            if nums[end] < left:
                res += window_count
            elif nums[end] > right:
                window_count = 0
                start = end + 1
            else:
                window_count = end - start + 1
                res += window_count
            end += 1
        return res

# Time Complexity  : O(n)
# Space Complexity : O(1)