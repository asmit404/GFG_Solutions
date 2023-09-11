"""
Title     : Lucky Numbers
Author    : Asmit Singh
Solved On   : 11 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def isLucky(self, n):
        k = 2
        while k <= n:
            if n % k == 0:
                return False
            n -= n // k
            k += 1
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)