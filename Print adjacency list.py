"""
Title     : Print adjacency list
Author    : Asmit Singh
Solved On   : 5 Sept 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        adj = {}
        for u, v in sorted(edges):
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        return [adj.get(i, []) for i in range(V)]

# Time Complexity: O(E log E)
# Space Complexity: O(V + E)