"""
Title     : Sum of dependencies in a graph
Author    : Asmit Singh
Solved On   : 28 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def sumOfDependencies(self, adj, V):
        return sum(len(i) for i in adj)

# Time Complexity  : O(V)
# Space Complexity : O(1)