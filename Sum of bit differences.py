"""
Title     : Sum of bit differences
Author    : Asmit Singh
Solved On   : 29 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def sumBitDifferences(self, arr, n):
        res = 0
        for i in range(32):
            countOnes = sum((val >> i) & 1 for val in arr)
            countZeros = n - countOnes
            res += countOnes * countZeros * 2
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)