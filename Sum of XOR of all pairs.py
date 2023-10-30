"""
Title     : Sum of XOR of all pairs
Author    : Asmit Singh
Solved On   : 30 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def sumXOR(self, arr, n):
        res = 0
        for i in range(32):
            ones = sum(1 for x in arr if x & (1 << i))
            res += ones * (n - ones) * (1 << i)
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)