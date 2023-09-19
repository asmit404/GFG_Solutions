"""
Title     : Find first set bit
Author    : Asmit Singh
Solved On   : 19 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def getFirstSetBit(self, n):
        cnt = 0
        while n:
            cnt += 1
            if n & 1:
                return cnt
            n >>= 1
        return 0

# Time Complexity: O(1)
# Space Complexity: O(1)