'''
Title     : Cutting Binary String
Author    : Asmit Singh
Solved On   : 16 May 2023
Solved Using   : Python3
'''

from math import inf, log
class Solution:
    def cuts(self, s):
        n = len(s)
        m = [inf]*n + [0]
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            x = 0
            for j in range(i, n):
                x = x*2 + int(s[j])
                if 5**int(log(x, 5)) == x:
                    m[i] = min(m[i], m[j+1] + 1)
        return m[0] if m[0] != inf else -1
