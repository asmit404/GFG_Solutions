"""
Title     : Panagram Checking
Author    : Asmit Singh
Solved On   : 01 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def checkPangram(self, s):
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        return not alphabet.difference(set(s.lower()))

# Time Complexity: O(n)
# Space Complexity: O(n)