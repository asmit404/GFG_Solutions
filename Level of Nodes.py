"""
Title     : Level of Nodes
Author    : Asmit Singh
Solved On   : 19 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def nodeLevel(self, V, adj, X):
        q, lvl, vis = [0] ,0 ,set()
        vis.add(0)
        while q:
            lvl += 1
            size = len(q)
            for _ in range(size):
                node = q.pop(0)
                for i in adj[node]:
                    if i not in vis:
                        if i == X:
                            return lvl
                        vis.add(i)
                        q.append(i)
        return -1

# Time Complexity: O(V+E)
# Space Complexity: O(V+E)