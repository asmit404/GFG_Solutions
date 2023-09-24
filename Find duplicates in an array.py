"""
Title     : Find duplicates in an array
Author    : Asmit Singh
Solved On   : 24 Sept 2023
Solved Using   : Python3
"""

from collections import Counter
class Solution:
    def duplicates(self, arr, n):
        counter = Counter(arr)
        ans = sorted([k for k, v in counter.items() if v > 1])
        return ans if ans else [-1]

# Time Complexity: O(n log n)
# Space Complexity: O(n)