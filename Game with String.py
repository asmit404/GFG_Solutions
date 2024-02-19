"""
Title     : Game with String
Author    : Asmit Singh
Solved On   : 19 Feb 2024
Solved Using   : Python3
"""

from heapq import heapify, heappop, heappush
class Solution:
    def minValue(self, s, k):
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        freqs = [-val for val in dic.values()]
        heapify(freqs)
        for _ in range(k):
            max_freq = heappop(freqs)
            if max_freq < 0:
                heappush(freqs, max_freq + 1)
        res = sum(i**2 for i in freqs)
        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)