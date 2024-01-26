"""
Title     : Fractional Knapsack
Author    : Asmit Singh
Solved On   : 26 Jan 2024
Solved Using   : Python3
"""

from heapq import heappush, heappop

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

class Solution:
    def fractionalknapsack(self, W, arr, n):
        h = []
        for i in range(n):
            val = arr[i].value
            w = arr[i].weight
            heappush(h, (-val/w, val, w))
        res = 0
        for _ in range(n):
            if not h:
                break
            _, val, w = heappop(h)
            if w <= W:
                res += val
                W -= w
            else:
                res += (W/w) * val
                break
        else:
            while h:
                _, val, w = heappop(h)
                if w <= W:
                    res += val
                    W -= w
                else:
                    res += (W/w) * val
                    break
        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)