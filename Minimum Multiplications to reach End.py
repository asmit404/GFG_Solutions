"""
Title     : Minimum Multiplications to reach End
Author    : Asmit Singh
Solved On   : 7 Sept 2023
Solved Using   : Python3
"""

from typing import List
from collections import deque

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        dist = [float('inf')]*(100000+1)
        q = deque([(start, 0)])
        visited = set([start])
        mod = 100000
        while q:
            ele, st = q.popleft()
            if ele == end:
                return st
            for j in arr:
                ele2 = (j*ele) % mod
                if ele2 not in visited:
                    visited.add(ele2)
                    dist[ele2] = st+1
                    q.append((ele2, st+1))
        return -1

# Time Complexity: O(N log N)
# Space Complexity: O(sqrt(N))