"""
Title     : Multiply two strings
Author    : Asmit Singh
Solved On   : 24 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def multiplyStrings(self, s1, s2):
        return str(int(s1)*int(s2))

# I think the Karatsuba algorithm would be faster but I'm too lazy to implement it.
# Time Complexity: O(N^2)
# Space Complexity: O(1)