"""
Title     : Minimize the Heights II
Author    : Asmit Singh
Solved On   : 05 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def getMinDiff(self, array, size, k):
        array.sort()
        res = array[size - 1] - array[0]
        for i in range(size):
            big = max(array[i - 1] + k, array[size - 1] - k) if i > 0 else array[size - 1] - k
            smol = min(array[i] - k, array[0] + k)
            if smol < 0: continue
            res = min(res, big - smol)
        return res

# Time Complexity  : O(nlogn)
# Space Complexity : O(1)