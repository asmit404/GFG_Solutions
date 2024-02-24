"""
Title     : Maximum Sum Problem
Author    : Asmit Singh
Solved On   : 24 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def maxSum(self, n):
        a, b, c = n // 2, n // 3, n // 4
        return self.maxSum(a)+self.maxSum(b)+self.maxSum(c) if (a + b + c) > n else n

# Time Complexity: O(n)
# Space Complexity: O(n)