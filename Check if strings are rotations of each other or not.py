"""
Title     : Check if strings are rotations of each other or not
Author    : Asmit Singh
Solved On   : 14 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def areRotations(self, s1, s2):
        return 1 if s1 in s2 * 2 else 0

# Time Complexity: O(n^2)
# Space Complexity: O(n)