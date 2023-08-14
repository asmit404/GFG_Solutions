"""
Title     : Non Repeating Numbers
Author    : Asmit Singh
Solved On   : 14 Aug 2023
Solved Using   : Python3
"""

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        store = Counter(nums)
        ans = tuple(i for i in store if store[i] == 1)
        return sorted(ans)

# Time Complexity : O(n)
# Space Complexity : O(n)