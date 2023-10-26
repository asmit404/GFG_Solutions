"""
Title     : Minimum Operations
Author    : Asmit Singh
Solved On   : 26 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def minOperation(self, n):
        res = 0
        while n > 0:
            res += n % 2 + 1
            n //= 2
        return res - 1

# Time Complexity: O(log(n))
# Space Complexity: O(1)