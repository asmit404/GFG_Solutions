"""
Title     : Euler circuit and Path
Author    : Asmit Singh
Solved On   : 29 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def isEulerCircuitExist(self, V, adj):
        res = sum(1 for i in range(V) if len(adj[i]) % 2 != 0)
        return 2 if res == 0 else 1 if res == 2 else 0

# Time Complexity  : O(V)
# Space Complexity : O(1)