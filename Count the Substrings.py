"""
Title     : Count the Substrings
Domain    : Strings, Data Structures
Author    : Asmit Singh
Solved On   : 29 Mar 2023
Solved Using   : Python3
"""

class Solution:
    def countSubstring(self, S):
        d = {0: 1}
        c = 0
        ans = 0
        for i in S:
            if ord('a') <= ord(i) <= ord('z'):
                c -= 1
            else:
                c += 1
            ans += d.get(c, 0)
            d[c] = d.get(c, 0) + 1
        return ans
