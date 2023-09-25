"""
Title     : Maximum Sum Combination
Author    : Asmit Singh
Solved On   : 25 Sept 2023
Solved Using   : Python3
"""

import heapq
class Solution:
    def maxCombinations(self, n, k, a, b):
        pool, heap = [], []
        a.sort()
        b.sort(reverse=True)

        for i in range(n):
            heapq.heappush(heap, [-(a[i]+b[0]), i, 0])

        while k:
            el, i, j = heapq.heappop(heap)
            pool.append(-el)
            if j+1 < n:
                heapq.heappush(heap, [-(a[i]+b[j+1]), i, j+1])
            k -= 1
        return pool

# Time Complexity: O(k log n)
# Space Complexity: O(n)