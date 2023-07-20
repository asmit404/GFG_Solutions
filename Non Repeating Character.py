"""
Title     : Non Repeating Character
Author    : Asmit Singh
Solved On   : 20 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def nonrepeatingCharacter(self, s):
        for i in s:
            if s.count(i) == 1:
                return i
        return "$"
