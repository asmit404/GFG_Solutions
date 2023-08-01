"""
Title     : DFS of graph
Author    : Asmit Singh
Solved On   : 01 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def dfsOfGraph(self, V, adj):
        visited, pool, stack = [False] * V, [], [0]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                pool.append(node)
                stack.extend(adj[node][::-1])
        return pool

# Time Complexity  : O(V + E)
# Space Complexity : O(V)