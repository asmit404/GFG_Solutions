'''
Title     : Topological Sort
Author    : Asmit Singh
Solved On   : 01 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def topoSort(self, V, adj):
        stack = []
        visited = [False] * V

        def dfs(vertex, visited, stack, adj):
            visited[vertex] = True
            for neighbour in adj[vertex]:
                if not visited[neighbour]:
                    dfs(neighbour, visited, stack, adj)
            stack.append(vertex)

        for vertex in range(V):
            if not visited[vertex]:
                dfs(vertex, visited, stack, adj)

        return stack[::-1]
