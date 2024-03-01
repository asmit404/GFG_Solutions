"""
Title     : Peak element
Author    : Asmit Singh
Solved On   : 01 Mar 2024
Solved Using   : Python3
"""

class Solution:
    def peakElement(self, arr, n):
        if len(arr) == 1: return 0
        if arr[0] >= arr[1]: return 0
        if arr[len(arr)-1] >= arr[len(arr)-2]: return len(arr) - 1
        for i in range(1, len(arr)-1):
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                return i

# Time Complexity: O(n)
# Space Complexity: O(1)