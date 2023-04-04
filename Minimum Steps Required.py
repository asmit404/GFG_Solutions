"""
Title     : Minimum Steps Required
Domain    : Greedy
Author    : Asmit Singh
Solved On   : 04 Apr 2023
Solved Using   : Python3
"""

class Solution:
    def minSteps(self, str: str) -> int:
        a, b = 0, 0
        str += '#'
        for i in range(len(str)-1):
            if (str[i] == 'a' and str[i+1] != 'a'):
                a += 1
        for i in range(len(str)-1):
            if (str[i] == 'b' and str[i+1] != 'b'):
                b += 1
        if (a < b):
            return a+1
        else:
            return b+1
