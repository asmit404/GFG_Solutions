'''
Title     : Is Binary Number Multiple of 3
Author    : Asmit Singh
Solved On   : 30 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def isDivisible(self, s):
        val = int(s, 2)
        return 1 if val % 3 == 0 else 0
