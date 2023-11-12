"""
Title     : Check if string is rotated by two places
Author    : Asmit Singh
Solved On   : 12 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def isRotated(self, str1, str2):
        if len(str1) != len(str2):
            return False

        n = len(str1)
        for i in range(n):
            if str1[i] != str2[(i+2) % n] and str1[i] != str2[(i-2) % n]:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)