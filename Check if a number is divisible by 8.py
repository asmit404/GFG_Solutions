"""
Title     : Check if a number is divisible by 8
Author    : Asmit Singh
Solved On   : 28 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def DivisibleByEight(self,s):
        return 1 if int(s[-3:]) % 8 == 0 else -1

# Time Limit Exceeded when using bitwise operations
# Time Complexity: O(1)
# Space Complexity: O(1)