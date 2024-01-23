"""
Title     : Course Schedule
Author    : Asmit Singh
Solved On   : 23 Jan 2024
Solved Using   : Python3
"""

from collections import defaultdict
class Solution:
    def findOrder(self, N, m, P):
        graph = defaultdict(list)
        res, vis = [], [0] * N
        for a, b in P:
            graph[a].append(b)

        def DFS(i):
            if vis[i]:
                return vis[i] == 1
            vis[i] = -1
            for node in graph[i]:
                if not DFS(node):
                    return False
            vis[i] = 1
            res.append(i)
            return True

        for node in range(N):
            if not DFS(node):
                return []
        return res

# Time Complexity: O(N + E)
# Space Complexity: O(N + E)