"""
Title     : Boolean Parenthesization
Author    : Asmit Singh
Solved On   : 21 Feb 2024
Solved Using   : Python3
"""

from functools import lru_cache
class Solution:
    def countWays(self, n, s):
        @lru_cache(None)
        def count(i, j, result=True):
            MOD = 1003
            res = 0
            if i == j:
                return int(s[i] == 'T') if result else int(s[i] == 'F')
            for k in range(i + 1, j, 2):
                if s[k] == '&':
                    if result:
                        res += count(i, k - 1, True) * count(k + 1, j, True)
                    else:
                        res += count(i, k - 1, False) * count(k + 1, j, False)
                        res += count(i, k - 1, False) * count(k + 1, j, True)
                        res += count(i, k - 1, True) * count(k + 1, j, False)
                if s[k] == '|':
                    if result:
                        res += count(i, k - 1, True) * count(k + 1, j, False)
                        res += count(i, k - 1, False) * count(k + 1, j, True)
                        res += count(i, k - 1, True) * count(k + 1, j, True)
                    else:
                        res += count(i, k - 1, False) * count(k + 1, j, False)
                if s[k] == '^':
                    if result:
                        res += count(i, k - 1, True) * count(k + 1, j, False)
                        res += count(i, k - 1, False) * count(k + 1, j, True)
                    else:
                        res += count(i, k - 1, False) * count(k + 1, j, False)
                        res += count(i, k - 1, True) * count(k + 1, j, True)
            return res % MOD
        return count(0, n - 1)

# Time Complexity: O(n ^ 3)
# Space Complexity: O(n ^ 2)