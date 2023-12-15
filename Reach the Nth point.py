"""
Title     : Reach the Nth point
Author    : Asmit Singh
Solved On   : 15 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def nthPoint(self, n):
        MOD = 1000000007
        a = b = 1
        for _ in range(1, n):
            a, b = b, (a+b) % MOD
        return b

# Time Complexity  : O(n)
# Space Complexity : O(1)