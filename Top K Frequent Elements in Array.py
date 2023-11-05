"""
Title     : Top K Frequent Elements in Array
Author    : Asmit Singh
Solved On   : 05 Nov 2023
Solved Using   : Python3
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        items = sorted(count.items(), key=lambda x: (-x[1], -x[0]))
        return [item[0] for item in items[:k]]

# Time Complexity: O(n log n)
# Space Complexity: O(n)