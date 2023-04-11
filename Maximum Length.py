"""
Title     : Maximum Length
Domain    : Strings, Data Structures
Author    : Asmit Singh
Solved On   : 11 Apr 2023
Solved Using   : Python3
"""

class Solution():
    def solve(self, a, b, c):
        k = [a,b,c]
        k.sort(reverse=True)
        if k[1]+k[2]>=(k[0]/2)-1:
            return a+b+c
        else:
            return -1
