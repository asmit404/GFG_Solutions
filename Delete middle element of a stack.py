'''
Title     : Implement two stacks in an array
Author    : Asmit Singh
Solved On   : 14 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def deleteMid(self, s, sizeOfStack):
        mid = (sizeOfStack + 1) // 2
        s.pop(mid - 1)
