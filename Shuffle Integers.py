"""
Title     : Shuffle Integers
Author    : Asmit Singh
Solved On   : 25 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def shuffleArray(self, arr, n):
        ctr, ptr = 1, n//2
        for _ in range(n//2):
            arr.insert(ctr, arr.pop(ptr))
            ptr += 1
            ctr += 2

# Time Complexity  : O(n^2)
# Space Complexity : O(1)