"""
Title     : Equal Left and Right Subarray Sum
Domain    : Prefix-Sum, Arrays, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 06 Apr 2023
Solved Using   : Python3
"""

class Solution:
    def equalSum(self, a, n):
        total = sum(a)
        var = 0
        for i in range(n):
            total -= a[i]
            if var == total:
                return i+1
            var += a[i]
        return -1
