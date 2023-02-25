'''
Title     : Shortest Path Using Atmost One Curved Edge
Domain    : Graph, Shortest Path, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 24 Feb 2023
Solved Using   : Python3
'''

from heapq import heappush, heappop
# Using Dijstra's Algorithm
INF = float('inf')
class Solution:
    def shortestPath(self, n, m, a, b, edges):
        from collections import defaultdict
        cu = []
        g = defaultdict(list)
        for (x, y, w1, w2) in edges:
            g[x].append((y, w1))
            g[y].append((x, w1))
            cu.append((x, y, w2))
            
        def dijkstra(x, y):
            nonlocal n, g
            ret = [INF]*(n+1)
            ret[x] = 0
            q = [(0, x)]
            while q:
                cost0, n0 = heappop(q)
                for nbr, w in g[n0]:
                    cost = cost0+w
                    if ret[nbr] > cost:
                        ret[nbr] = cost
                        heappush(q, (cost, nbr))
            return ret
            
        da = dijkstra(a, b)
        db = dijkstra(b, a)
        ans = da[b]
        for u, v, w in cu:
            ans = min(ans, da[u]+w+db[v])
            ans = min(ans, da[v]+w+db[u])
        return -1 if ans == INF else ans
