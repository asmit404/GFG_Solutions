"""
Title     : Transitive closure of a Graph
Author    : Asmit Singh
Solved On   : 17 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def transitiveClosure(self, N, graph):
        def dfs(start_vertex):
            vis.add(start_vertex)
            for adj in range(len(graph[start_vertex])):
                if graph[start_vertex][adj] == 1 and adj not in vis:
                    dfs(adj)

        tc = [[0]*N for _ in range(N)]
        for i in range(len(graph)):
            vis = set()
            dfs(i)
            for j in vis:
                tc[i][j] = 1
        return tc

# Time Complexity: O(n^3)
# Space Complexity: O(n^2)