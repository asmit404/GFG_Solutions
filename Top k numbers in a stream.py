"""
Title     : Top k numbers in a stream
Author    : Asmit Singh
Solved On   : 19 Jan 2024
Solved Using   : Python3
"""

from collections import defaultdict
class Solution:
    def kTop(self, arr, N, K):
        dic, res = defaultdict(int), []
        for a in arr:
            dic[a] += 1
            k = list(dic.keys())
            k.sort(key=lambda x: (-dic[x], x))
            i = k.index(0) if 0 in k else N
            res.append(k[:min(K, i)])
        return res

# Time Complexity: O(N^2 * log(N))
# Space Complexity: O(N)