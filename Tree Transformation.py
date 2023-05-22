'''
Title     : Tree Transformation
Author    : Asmit Singh
Solved On   : 22 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def solve(self, N: int, p: List[int]) -> int:
        nodes = [0] * N
        for i in range(1, N):
            nodes[p[i]] += 1
            nodes[i] += 1
        leaves = nodes.count(1)
        return max(N - leaves - 1, 0)
