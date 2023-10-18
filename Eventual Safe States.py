"""
Title     : Eventual Safe States
Author    : Asmit Singh
Solved On   : 18 Oct 2023
Solved Using   : Python3
"""

from typing import List

class Solution:
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        def is_safe(node):
            if node in safe:
                return True
            if node in vis:
                return False

            vis.add(node)
            if all(is_safe(neighbor) for neighbor in adj[node]):
                safe.add(node)
                return True
            vis.remove(node)
            return False

        safe, vis = set(), set()
        for node in range(V):
            is_safe(node)
        return sorted(list(safe))

# Time Complexity: O(V+E)
# Space Complexity: O(V+E)