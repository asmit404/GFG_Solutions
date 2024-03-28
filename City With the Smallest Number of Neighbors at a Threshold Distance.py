'''
Title     : City With the Smallest Number of Neighbors at a Threshold Distance
Author    : Asmit Singh
Solved On   : 28 Mar 2024
Solved Using   : Python3
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def dijkstra(self, v, adj, s):
        dist = [float("inf")]*v
        pq = [(0, s)]
        dist[s] = 0
        while pq:
            dis, node = heappop(pq)
            for i in adj[node]:
                adjwt = i[1]
                adjnode = i[0]
                if adjwt + dis < dist[adjnode]:
                    dist[adjnode] = adjwt+dis
                    heappush(pq, (dist[adjnode], adjnode))
        return dist

    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for i in edges:
            adj[i[0]].append((i[1], i[2]))
            adj[i[1]].append((i[0], i[2]))
        citycount = 100
        citynum = -1
        for c in range(n):
            dist = self.dijkstra(n, adj, c)
            count = 0
            for adjcity in dist:
                if adjcity <= distanceThreshold:
                    count += 1
            if count <= citycount:
                citycount = count
                citynum = c
        return citynum

# Time Complexity: O(E log E)
# Space Complexity: O(V + E)