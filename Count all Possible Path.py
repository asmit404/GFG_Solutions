"""
Title     : Count all Possible Path
Author    : Asmit Singh
Solved On   : 15 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def isPossible(self, paths):
        return int(all(sum(row) % 2 == 0 for row in paths))

# Time Complexity: O(nm)
# Space Complexity: O(1)