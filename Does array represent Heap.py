"""
Title     : Does array represent Heap
Author    : Asmit Singh
Solved On   : 17 Feb 2024
Solved Using   : Python3
"""

from heapq import heapify
class Solution:
    def isMaxHeap(self,arr,n):
        pool = [-i for i in arr]
        heapify(pool)
        maxheap = [-i for i in pool]
        return int(maxheap == arr)

# Time Complexity: O(n)
# Space Complexity: O(n)