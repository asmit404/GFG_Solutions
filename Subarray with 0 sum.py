"""
Title     : Subarray with 0 sum
Author    : Asmit Singh
Solved On   : 10 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def subArrayExists(self, arr, n):
        sum_map, res = {0: -1}, 0
        for i in range(n):
            res += arr[i]
            if res in sum_map:
                return arr[sum_map[res] + 1: i + 1]
            sum_map[res] = i
        return []

# Time Complexity  : O(n)
# Space Complexity : O(n)