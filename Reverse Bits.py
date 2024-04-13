'''
Title     : Reverse Bits
Author    : Asmit Singh
Solved On   : 13 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def reversedBits(self, x, res = 0):
        for _ in range(32):
            res = (res << 1) | (x & 1)
            x >>= 1
        return res

# Time Complexity: O(1)
# Space Complexity: O(1)