'''
Title     : Copy Set Bits in Range
Author    : Asmit Singh
Solved On   : 2 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def setSetBit(self, res, y, l, r):
        for i in range(l, r + 1):
            bit_value = y & (1 << (i - 1))
            res = res | bit_value
        return res
