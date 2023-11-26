"""
Title     : Print Pattern
Author    : Asmit Singh
Solved On   : 26 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def pattern(self, N):
        if N <= 0:
            return [N,]
        a = list(range(N, -5, -5))
        return a + a[::-1][1:]

# Time Complexity  : O(n)
# Space Complexity : O(n)