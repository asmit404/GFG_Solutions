'''
Title     : String rp or pr
Domain    : Strings, Greedy, Stack, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 22 Mar 2023
Solved Using   : Python3
'''

class Solution:
    def solve(self, X, Y, S):
        if X >= Y:
            order = [('pr', X), ('rp', Y)]
        else:
            order = [('rp', Y), ('pr', X)]
        ans = 0
        for (c0, c1), score in order:
            N, l = len(S), []
            for i in range(N):
                l.append(S[i])
                if S[i] == c1 and len(l) > 1 and l[-2] == c0:
                    ans += score
                    l.pop()
                    l.pop()
            S = l
        return ans
