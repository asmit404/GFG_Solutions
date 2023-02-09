'''
Title     : Maximum Bipartite Matching
Domain    : Graph, Data Structures
Author    : Asmit Singh
Solved On   : 09 Feb 2023
Solved Using   : Python3
'''

class Solution:
      def maximumMatch(self,G):
        m, n = len(G), len(G[0])
        match = [-1] * n
        v = [False] * n
        def dfs(i):
            for j in range(n):
                if G[i][j] and not v[j]:
                    v[j] = True
                    if match[j] == -1 or dfs(match[j]):
                        match[j] = i
                        return True
            return False
        c = 0
        for i in range(m):
            v = [False] * n
            if dfs(i):
                c += 1
        return c
