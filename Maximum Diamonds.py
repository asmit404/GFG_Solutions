'''
Title     : Maximum Diamonds
Author    : Asmit Singh
Solved On   : 14 Jun 2023
Solved Using   : Python3
'''

import heapq
class Solution:
    def maxDiamonds(self, A, N, K):
        dia = 0
        pool = [-num for num in A]
        heapq.heapify(pool)

        for i in range(K):
            maxElement = -heapq.heappop(pool)
            dia += maxElement
            heapq.heappush(pool, -(maxElement // 2))

        return dia
