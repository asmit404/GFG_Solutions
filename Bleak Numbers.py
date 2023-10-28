"""
Title     : Bleak Numbers
Author    : Asmit Singh
Solved On   : 28 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def is_bleak(self, n):
        def count_set_bit(num):
            return bin(num).count('1')

        for i in range(n-30, n+1):
            if i + count_set_bit(i) == n:
                return 0
        return 1

# Time Complexity: O(n)
# Space Complexity: O(1)