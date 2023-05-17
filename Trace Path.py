'''
Title     : Trace Path
Author    : Asmit Singh
Solved On   : 17 May 2023
Solved Using   : Python3
'''

class Solution:
    def isPossible(self, n, m, s):
        h, w, minw, maxw, minh, maxh = 0, 0, 0, 0, 0, 0
        for k in s:
            if k == 'L':
                w -= 1
                minw = min(w, minw)
            if k == 'R':
                w += 1
                maxw = max(w, maxw)
            if k == 'U':
                h -= 1
                minh = min(h, minh)
            if k == 'D':
                h += 1
                maxh = max(h, maxh)
        if maxh - minh >= n:
            return 0
        if maxw - minw >= m:
            return 0
        return 1
