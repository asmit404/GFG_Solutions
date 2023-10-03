"""
Title     : Column name from a given column number
Author    : Asmit Singh
Solved On   : 3 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def colName(self, n):
        res = ""
        while n > 0:
            n -= 1
            res += chr(ord('A') + n % 26)
            n //= 26
        return res[::-1]

# Time Complexity: O(log n)
# Space Complexity: O(1)