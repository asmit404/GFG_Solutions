"""
Title     : Find the closest pair from two arrays
Author    : Asmit Singh
Solved On   : 27 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def printClosest(self, arr, brr, n, m, x):
        arr.sort()
        brr.sort()
        i, j = 0, m-1
        diff = float('inf')
        a, b = -1, -1
        while i < n and j >= 0:
            s = arr[i] + brr[j]
            if abs(s - x) < diff:
                diff = abs(s - x)
                a, b = arr[i], brr[j]
            if s > x:
                j -= 1
            else:
                i += 1
        return [a, b]

# Time Complexity: O(nlogn + mlogm)
# Space Complexity: O(1)