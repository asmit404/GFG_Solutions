'''
Title     : Find k-th smallest element in given n ranges
Author    : Asmit Singh
Solved On   : 19 May 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def kthSmallestNum(self, n: int, ranges: List[List[int]], q: int, queries: List[int]) -> List[int]:
        ranges.sort()
        skip = [0] * n
        count = [0] * n
        if ranges[0][0] > 1:
            skip[0] = ranges[0][0] - 1
        count[0] = ranges[0][1] - ranges[0][0] + 1
        for i in range(1, n):
            gap = ranges[i][0] - ranges[i - 1][1] - 1
            skip[i] = skip[i - 1] + max(0, gap)
            count[i] = count[i - 1]
            if ranges[i - 1][1] >= ranges[i][0]:
                count[i] += ranges[i][1] - ranges[i - 1][1] + 1
            else:
                count[i] += ranges[i][1] - ranges[i][0] + 1

        ans = [-1] * q
        for i in range(q):
            idx = -1
            for j in range(n):
                if queries[i] <= count[j]:
                    idx = j
                    break
            if idx != -1:
                ans[i] = skip[idx] + queries[i]
        return ans
