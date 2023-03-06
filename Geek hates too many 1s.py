'''
Title     : Geeks hates too many 1s
Domain    : Bit Magic, Data Structures
Author    : Asmit Singh
Solved On   : 6 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def noConseBits(self, n: int) -> int:
        c = 0
        for i in range(31, -1, -1):
            if n & (1 << i):
                c += 1
            else:
                c = 0
            if c == 3:
                n &= (~(1 << i))
                c = 0
        return n
