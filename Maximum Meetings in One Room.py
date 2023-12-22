"""
Title     : Maximum Meetings in One Room
Author    : Asmit Singh
Solved On   : 22 Dec 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def maxMeetings(self, n: int, s: List[int], f: List[int]) -> List[int]:
        pool = sorted([[s[i], f[i], i + 1] for i in range(n)], key = lambda j: (j[1], j[2]))
        res = [pool[0][2]]
        for i in pool[1:]:
            if i[0] > f[res[-1] - 1]:
                res.append(i[2])
        return sorted(res)

# Time Complexity  : O(nlogn)
# Space Complexity : O(n)