"""
Title     : Minimum distance between two numbers
Author    : Asmit Singh
Solved On   : 02 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def minDist(self, arr, n, x, y):
        min_dist, p = float('inf'), -1
        for i, val in enumerate(arr):
            if val in {x, y}:
                if p != -1 and val != arr[p]:
                    min_dist = min(min_dist, i - p)
                p = i
        return -1 if min_dist == float('inf') else min_dist

# Time Complexity: O(n)
# Space Complexity: O(1)