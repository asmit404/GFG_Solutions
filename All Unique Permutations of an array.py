"""
Title     : All Unique Permutations of an array
Author    : Asmit Singh
Solved On   : 17 Jan 2024
Solved Using   : Python3
"""

from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        return sorted(list(set(permutations(arr, n))))

# Time Complexity: O(n!)
# Space Complexity: O(n!)