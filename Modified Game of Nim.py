"""
Title     : Modified Game of Nim
Author    : Asmit Singh
Solved On   : 20 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def findWinner(self, n, A):
        xor = 0
        for num in A:
            xor ^= num
        return (n % 2) + 1 if xor else 1

# Time Complexity  : O(n)
# Space Complexity : O(1)