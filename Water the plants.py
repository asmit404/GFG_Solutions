"""
Title     : Water the plants
Author    : Asmit Singh
Solved On   : 18 Jan 2024
Solved Using   : Python3
"""

from collections import deque
class Solution:
    def min_sprinklers(self, gallery, n):
        pool = deque(sorted([(i - g, i + g) for i, g in enumerate(gallery) if g != -1]))
        reachable = best = res = 0
        while reachable < n:
            if pool and pool[0][0] <= reachable:
                _, e = pool.popleft()
                best = max(best, e+1)
            elif best > reachable:
                reachable = best
                res += 1
            else:
                return -1
        return res

# Time Complexity: O(n log n)
# Space Complexity: O(n)