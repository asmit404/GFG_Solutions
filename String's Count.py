"""
Title     : String's Count
Author    : Asmit Singh
Solved On   : 16 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def countStr(self, n):
        return int(1 + (n * 2) + n * ((n * n) - 1) / 2)

# Time Complexity  : O(1)
# Space Complexity : O(1)