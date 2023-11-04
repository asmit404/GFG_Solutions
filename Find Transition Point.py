"""
Title     : Find Transition Point
Author    : Asmit Singh
Solved On   : 04 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def transitionPoint(self, arr, n):
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
                return mid
            elif arr[mid] == 0:
                start = mid + 1
            else:
                end = mid - 1
        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)