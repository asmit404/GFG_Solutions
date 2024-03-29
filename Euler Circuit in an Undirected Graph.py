'''
Title     : Euler Circuit in an Undirected Graph
Author    : Asmit Singh
Solved On   : 29 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def isEularCircuitExist(self, v, adj):
        return all(len(adj[i]) % 2 == 0 for i in range(v))

# Time Complexity: O(V)
# Space Complexity: O(1)