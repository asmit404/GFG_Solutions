"""
Title     : Find element occuring once when all other are present thrice
Author    : Asmit Singh
Solved On   : 4 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def singleElement(self, arr, N):
        ones, twos = 0, 0
        for num in arr:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

# Time Complexity  : O(n)
# Space Complexity : O(1)