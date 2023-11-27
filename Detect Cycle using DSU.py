"""
Title     : Detect Cycle using DSU
Author    : Asmit Singh
Solved On   : 27 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def find(self, n, parent):
        if parent[n] == n:
            return n
        parent[n] = self.find(parent[n], parent)
        return parent[n]

    def union(self, a, b, parent):
        x = self.find(a, parent)
        y = self.find(b, parent)
        if x != y:
            parent[x] = y
            return False
        return True

    def detectCycle(self, V, adj):
        parent = list(range(V))
        for i in range(V):
            for j in adj[i]:
                if i < j and self.union(i, j, parent):
                    return 1
        return 0

# Time Complexity  : O(V+E)
# Space Complexity : O(V)