'''
Title     : Array Operations
Author    : Asmit Singh
Solved On   : 12 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def arrayOperations(self, n: int, arr: List[int]) -> int:
        if 0 not in arr:
            return -1
        c = 0
        for i in range(1, len(arr)):
            if arr[i-1] != 0 and arr[i] == 0:
                c += 1
        if arr[-1] != 0:
            c += 1
        return c
