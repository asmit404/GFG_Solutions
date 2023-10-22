"""
Title     : Number of paths
Author    : Asmit Singh
Solved On   : 22 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def numberOfPaths(self, m, n):
        path = 1
        MOD = 1000000007
        for i in range(m - 1):
            path = (path*(i+n)*pow(i+1, MOD-2, MOD)) % MOD
        return path

# Time Complexity: O(M)
# Space Complexity: O(1)