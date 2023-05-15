'''
Title     : Count Total Setbits
Author    : Asmit Singh
Solved On   : 15 May 2023
Solved Using   : Python3
'''

class Solution:
    def countBits(self, N: int) -> int:
        res = 0
        for i in range(31):
            a = 1 << i
            b = (N + 1) // (a * 2) * a
            c = (N + 1) % (a * 2) - a
            res += b + max(c, 0)
        return res
