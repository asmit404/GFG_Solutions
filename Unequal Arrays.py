'''
Title     : Unequal Arrays
Domain    : Arrays, Algorithms, Logical Thinking
Author    : Asmit Singh
Solved On   : 16 Apr 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def solve(self, N: int, a: List[int], b: List[int]) -> int:
        if sum(a) != sum(b):
            return -1
        a.sort()
        b.sort()
        ae, ao, be, bo = [], [], [], []
        for i in range(N):
            if a[i] % 2:
                ao.append(a[i])
            else:
                ae.append(a[i])
            if b[i] % 2:
                bo.append(b[i])
            else:
                be.append(b[i])
        if len(ao) != len(bo) or len(ae) != len(be):
            return -1
        osum, esum = 0, 0
        for i in range(len(ao)):
            osum += abs(ao[i]-bo[i])
        for i in range(len(ae)):
            esum += abs(ae[i]-be[i])
        if osum % 2 or esum % 2:
            return -1
        else:
            return ((osum+esum)//2)//2
