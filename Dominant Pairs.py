"""
Title     : Dominant Pairs
Domain    : Two-Pointer-Algorithm, Sorting, Algorithms
Author    : Asmit Singh
Solved On   : 12 Apr 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def dominantPairs(self, n: int, arr: List[int]) -> int:
        arr[:n//2] = sorted(arr[:n//2])
        arr[n//2:] = sorted(arr[n//2:])
        i = 0
        j = n//2
        count = 0
        while i < n//2 and j < n:
            if arr[i] >= 5*arr[j]:
                count += n//2-i
                j += 1
            else:
                i += 1
        return count
