"""
Title     : Check if a given graph is tree or not
Author    : Asmit Singh
Solved On   : 24 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def isCyclePresent(self, node, adj, vis, p):
        vis.add(node)
        for i in adj[node]:
            if i == p:
                continue
            if i in vis or not self.isCyclePresent(i, adj, vis, node):
                return False
        return True

    def isTree(self, n, m, edges):
        adj, vis = [[] for _ in range(n)], set()
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        return int(self.isCyclePresent(0, adj, vis, -1) and len(vis) == n)

# Time Complexity: O(N)
# Space Complexity: O(N)