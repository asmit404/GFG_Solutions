"""
Title     : Vertex Cover
Author    : Asmit Singh
Solved On   : 21 Jan 2024
Solved Using   : Python3
"""

from typing import List
class Solution:
    def vertexCover(self, n: int, edges: List[List[int]]) -> int:
        def compute(edges):
            if not edges: return 0
            ed0 = [i for i in edges if i[0] != edges[0][0] and i[1] != edges[0][0]]
            ed1 = [i for i in edges if i[0] != edges[0][1] and i[1] != edges[0][1]]
            return min(1 + compute(ed0), 1 + compute(ed1))
        return compute(edges)

# Time Complexity: O(2^N)
# Space Complexity: O(N)