"""
Title     : Recursive sequence
Author    : Asmit Singh
Solved On   : 12 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def sequence(self, n):
        MOD = 1000000007
        res, curr = 0, 1
        for i in range(1, n + 1):
            sm = curr
            for _ in range(1, i):
                curr += 1
                sm *= curr
            res += sm
            curr += 1
        return res % MOD

# Time Complexity: O(n^2)
# Space Complexity: O(1)