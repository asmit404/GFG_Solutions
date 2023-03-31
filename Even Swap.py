"""
Title     : Even Swap
Domain    : Arrays, Sorting, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 31 Mar 2023
Solved Using   : Python3
"""

import numpy as np
class Solution():
    def lexicographicallyLargest(self, a, n):
        arr = np.array(a)
        i = 0
        while i < n:
            j = i+1
            while j < n and arr[j-1] % 2 == arr[j] % 2:
                j += 1
            arr[i:j].sort()
            arr[i:j] = arr[i:j][::-1]
            i = j
        a = arr.tolist()
        return a
