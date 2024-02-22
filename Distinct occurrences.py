"""
Title     : Distinct occurrences
Author    : Asmit Singh
Solved On   : 22 Feb 2024
Solved Using   : Python3
"""

from functools import lru_cache
class Solution:
    def sequenceCount(self, s, t):
        MOD = 1000000007
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            return ((dfs(i + 1, j + 1) + dfs(i + 1, j)) if s[i] == t[j] else dfs(i + 1, j)) % MOD
        return dfs(0, 0)

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)