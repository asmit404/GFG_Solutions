"""
Title     : Find the String
Author    : Asmit Singh
Solved On   : 16 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def build_graph(self, N, K):
        graph = {}
        strings = [''.join(str((j // K ** i) % K)
                           for i in range(N)) for j in range(K ** N)]
        for s in strings:
            graph[s] = [s[1:] + str(i)
                        for i in range(K) if s[1:] + str(i) != s]
        return graph, strings

    def findString(self, N, K):
        graph, strings = self.build_graph(N, K)
        visited = set()

        def find(s, current_string):
            visited.add(s)
            if len(visited) == K ** N:
                return current_string
            for neighbor in graph[s]:
                if neighbor not in visited:
                    result = find(neighbor, current_string + neighbor[-1])
                    if result:
                        return result
            visited.remove(s)

        for s in strings:
            result = find(s, s)
            if result:
                return result

# Time Complexity : O(K^N * N)
# Space Complexity: O(K^N * N)