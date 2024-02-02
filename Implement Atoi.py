"""
Title     : Implement Atoi
Author    : Asmit Singh
Solved On   : 02 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def atoi(self, s):
        try:
            return int(s)
        except ValueError:
            return -1

# Time Complexity: O(n)
# Space Complexity: O(1)