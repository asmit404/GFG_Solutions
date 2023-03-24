'''
Title     : Remove and Reverse
Domain    : Two-Pointer-Algorithm, Arrays, Strings, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 24 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def removeReverse(self, s):
        h, d = [0]*26, 1
        for i in range(len(s)):
            h[ord(s[i])-97] += 1
        i = 0
        while (0 <= i < len(s)):
            if (h[ord(s[i])-97]) > 1:
                h[ord(s[i])-97] -= 1
                s = s[:i]+s[i+1:]
                i = len(s)-1 if d == 1 else 0
                d *= -1
            else:
                i += d
        return s if d > 0 else s[::-1]
