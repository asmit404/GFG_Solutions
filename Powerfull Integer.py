'''
Title     : Powerfull Integer
Author    : Asmit Singh
Solved On   : 30 Apr 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def powerfullInteger(self, n: int, intervals: List[List[int]], k: int) -> int:
        arr = []
        n = 0
        res = -1
        for n1, n2 in intervals:
            arr.append((n1, -1))
            arr.append((n2, 1))
        arr.sort()
        for n1, n2 in arr:
            if n2 == -1:
                n += 1
            else:
                if n >= k:
                    res = max(res, n1)
                n -= 1
        return res
