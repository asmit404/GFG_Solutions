"""
Title     : Shortest path in Directed Acyclic Graph
Author    : Asmit Singh
Solved On   : 03 Aug 2023
Solved Using   : Python3
"""

import math
from typing import List

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        indegrees = [0] * n
        dist = [math.inf] * n
        dist[0] = 0

        for u, v, d in edges:
            adj[u].append((v, d))
            indegrees[v] += 1

        queue = [i for i in range(n) if indegrees[i] == 0]
        while queue:
            u = queue.pop(0)
            for v, d in adj[u]:
                alt = dist[u] + d
                if alt < dist[v]:
                    dist[v] = alt
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    queue.append(v)

        return [-1 if val == math.inf else val for val in dist]

# Time Complexity : O(n + m)
# Space Complexity : O(n)