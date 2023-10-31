"""
Title     : Move all zeroes to end of array
Author    : Asmit Singh
Solved On   : 31 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def pushZerosToEnd(self, arr, n):
        arr.sort(key=lambda x: x == 0)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)