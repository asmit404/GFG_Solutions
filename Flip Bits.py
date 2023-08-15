"""
Title     : Flip Bits
Author    : Asmit Singh
Solved On   : 15 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def maxOnes(self, a, n):
        zero = maxi = one = 0
        for i in range(n):
            if a[i] == 0:
                zero += 1
            else:
                zero -= 1
                one += 1
            maxi = max(zero, maxi)
            if zero < 0:
                zero = 0
        return maxi + one

# Time Complexity: O(n)
# Space Complexity: O(1)