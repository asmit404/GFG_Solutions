"""
Title     : Largest Number formed from an Array
Author    : Asmit Singh
Solved On   : 03 Mar 2024
Solved Using   : Python3
"""

from functools import cmp_to_key
class Solution:
    def printLargest(self, n, arr):
        arr = sorted(map(str, arr), key = cmp_to_key(
            lambda a, b: -1 if a + b > b + a else 1))
        return "".join(arr)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)