'''
Title     : Possible Paths in a Tree
Author    : Asmit Singh
Solved On   : 19 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def maximumWeight(self, n, edges, q, queries):
        store, sz = list(range(n+1)), [1] * (n+1)
        sz[0] = 0

        def find(i): return store[i] if store[i] == i else find(store[i])
        edges.sort(key=lambda x: x[2])
        queries = sorted(enumerate(queries), key=lambda x: x[1])

        ans, acc, start = [0] * len(queries), 0, 0
        for i, q in queries:
            while start < len(edges) and edges[start][2] <= q:
                x, y, _ = edges[start]
                rx, ry = find(x), find(y)
                if rx != ry:
                    acc += sz[rx]*sz[ry]
                    sz[rx] += sz[ry]
                    sz[ry] = 0
                    store[ry] = rx
                start += 1
            ans[i] = acc
        return ans

# Time Complexity: O((n + m) log m)
# Space Complexity: O(n + m)