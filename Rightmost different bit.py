"""
Title     : Rightmost different bit
Author    : Asmit Singh
Solved On   : 19 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def posOfRightMostDiffBit(self, m, n):
        xor = m ^ n
        return -1 if xor == 0 else (xor & -xor).bit_length()

# Time Complexity  : O(1)
# Space Complexity : O(1)