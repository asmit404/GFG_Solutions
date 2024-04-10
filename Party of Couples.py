'''
Title     : Party of Couples
Author    : Asmit Singh
Solved On   : 10 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def findSingle(self, n, arr):
        res = 0
        for item in arr:
            res ^= item
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)