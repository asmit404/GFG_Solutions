"""
Title     : Mother Vertex
Author    : Asmit Singh
Solved On   : 6 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def findMotherVertex(self, V, adj):
        vis = [False]*V
        pool = []
        for i in range(V):
            if not vis[i]:
                self.fill_order(adj, i, vis, pool)
        vis = [False]*V
        last_vis = pool[-1]
        self.dfs(adj, last_vis, vis)
        if False in vis:
            return -1
        return last_vis

    def fill_order(self, adj, V, vis, pool):
        vis[V] = True
        for neighbor in adj[V]:
            if not vis[neighbor]:
                self.fill_order(adj, neighbor, vis, pool)
        pool.append(V)

    def dfs(self, adj, V, vis):
        vis[V] = True
        for neighbor in adj[V]:
            if not vis[neighbor]:
                self.dfs(adj, neighbor, vis)

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)