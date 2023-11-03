"""
Title     : Pythagorean Triplet
Author    : Asmit Singh
Solved On   : 03 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def checkTriplet(self, arr, n):
        squares = {x**2 for x in arr}
        return any((a**2 + b**2 in squares) for a in arr for b in arr if a != b)

# Time Complexity: O(n^2)
# Space Complexity: O(n)