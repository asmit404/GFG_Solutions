"""
Title     : Frequencies of Limited Range Array Elements
Author    : Asmit Singh
Solved On   : 01 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def frequencyCount(self, arr, N, P):
        res = [0] * N
        min_val = min(P, N)
        for num in arr:
            if num <= min_val:
                res[num-1] += 1
        arr[:N] = res

# Time Complexity: O(n)
# Space Complexity: O(n)