"""
Title     : Palindrome String
Author    : Asmit Singh
Solved On   : 25 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def isPalindrome(self, S):
        return 1 if S == S[::-1] else 0

# Time Complexity: O(N)
# Space Complexity: O(N)