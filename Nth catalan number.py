"""
Title     : Nth catalan number
Author    : Asmit Singh
Solved On   : 16 Aug 2023
Solved Using   : Python3
"""

import math
class Solution:
    def findCatalan(self, n: int) -> int:
        res = math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))
        mod = 1000000007
        return res % mod

# Time Complexity: O(n)
# Space Complexity: O(1)