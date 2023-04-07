"""
Title     : Add Minimum Characters
Domain    : Strings, Data Structures
Author    : Asmit Singh
Solved On   : 07 Apr 2023
Solved Using   : Python3
"""

class Solution:
    def addMinChar(self, str1):
        if str1 == str1[::-1]:
            return 0
        i = 0
        j = len(str1)-1
        ans = j
        while i <= j:
            if str1[i] == str1[j]:
                j -= 1
                i += 1
            else:
                ans -= 1
                i = 0
                j = ans
        return len(str1)-(ans+1)
