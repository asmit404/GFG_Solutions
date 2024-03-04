"""
Title     : Swap the array elements
Author    : Asmit Singh
Solved On   : 04 Mar 2024
Solved Using   : Python3
"""

class Solution:
    def swapElements(self, arr, n):
        for i in range(n - 2):
            arr[i], arr[i+2] = arr[i+2], arr[i]
        return arr

# Time Complexity: O(n)
# Space Complexity: O(1)