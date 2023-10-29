"""
Title     : Check whether K-th bit is set or not
Author    : Asmit Singh
Solved On   : 29 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def checkKthBit(self, n, k):
        return (n >> k) & 1

# Time Complexity: O(1)
# Space Complexity: O(1)