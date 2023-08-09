"""
Title     : Largest prime factor
Author    : Asmit Singh
Solved On   : 09 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def largestPrimeFactor(self, N):
        ans = float('-inf')
        start = 2
        while start*start <= N:
            while N % start == 0:
                ans = start
                N //= start
            start += 1
        if (N > 1):
            return N
        return ans

# Time Complexity : O(sqrt(n))
# Space Complexity : O(1)