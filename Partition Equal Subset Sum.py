"""
Title     : Partition Equal Subset Sum
Author    : Asmit Singh
Solved On   : 15 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def equalPartition(self, N, arr):
        s = sum(arr)
        if s % 2 != 0:
            return False
        s //= 2
        dp = {0}
        for item in arr:
            dp |= {item + i for i in dp if item + i <= s}
        return s in dp

# Time Complexity: O(N * sum(arr))
# Space Complexity: O(sum(arr))