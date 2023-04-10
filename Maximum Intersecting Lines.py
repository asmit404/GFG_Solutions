"""
Title     : Maximum Intersecting Lines
Domain    : Mathematical, Sorting, Geometric, Algorithms
Author    : Asmit Singh
Solved On   : 10 Apr 2023
Solved Using   : Python3
"""

class Solution:
    def maxIntersections(self, lines, N):
        q = {}
        for i in lines:
            q[i[0]] = q.get(i[0], 0)+1
            q[i[1]+1] = q.get(i[1]+1, 0)-1
        ps = 0
        mx = 1
        for i in sorted(q):
            ps += q[i]
            mx = max(mx, ps)
        return mx
