'''
Title     : Count ways to Nth Stair
Author    : Asmit Singh
Solved On   : 6 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def countWays(self, n):
        return ((n // 2) + 1) % 1000000007

# Time Complexity: O(1)
# Space Complexity: O(1)