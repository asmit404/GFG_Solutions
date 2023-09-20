"""
Title     : Rotate Bits
Author    : Asmit Singh
Solved On   : 20 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def rotate(self, N, D):
        D = D % 16
        bin_str = format(N, '016b')
        left = bin_str[D:] + bin_str[:D]
        right = bin_str[-D:] + bin_str[:-D]
        return int(left, 2), int(right, 2)

# IDK how to use bitwise operators.
# Time Complexity: O(1)
# Space Complexity: O(1)