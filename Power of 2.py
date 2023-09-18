"""
Title     : Power of 2
Author    : Asmit Singh
Solved On   : 18 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def isPowerofTwo(self, n):
        return n != 0 and (n & (n - 1)) == 0

# Time Complexity: O(1)
# Space Complexity: O(1)