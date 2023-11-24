"""
Title     : Pascal Triangle
Author    : Asmit Singh
Solved On   : 24 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def nthRowOfPascalTriangle(self, n):
        MOD = 1000000007
        row = [1]
        for _ in range(n - 1):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return [x % MOD for x in row]

# Time Complexity  : O(n^2)
# Space Complexity : O(n)