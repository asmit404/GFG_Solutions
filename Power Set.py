"""
Title     : Power Set
Author    : Asmit Singh
Solved On   : 26 Feb 2024
Solved Using   : Python3
"""

from itertools import combinations
class Solution:
    def AllPossibleStrings(self, s):
        pool = []
        for i in range(1, len(s) + 1):
            for subs in combinations(s, i):
                pool.append(''.join(subs))
        return sorted(pool)

# Time Complexity: O(n * 2 ^ n)
# Space Complexity: O(n * 2 ^ n)