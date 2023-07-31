"""
Title     : BFS of graph
Author    : Asmit Singh
Solved On   : 31 Jul 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        queue, visited, result = [0], [0], []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for i in adj[node]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return result
