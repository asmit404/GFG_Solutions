"""
Title     : Find all Critical Connections in the Graph
Author    : Asmit Singh
Solved On   : 14 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def criticalConnections(self, v, adj):
        def dfs(u, parent):
            nonlocal time
            disc[u] = low[u] = time
            time += 1
            for v in adj[u]:
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((min(u, v), max(u, v)))
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        disc, low = [-1] * v, [-1] * v
        time, bridges = 0, []
        [dfs(i, -1) for i in range(v) if disc[i] == -1]
        return sorted(bridges)

# Time Complexity: O(V + E)
# Space Complexity: O(V)