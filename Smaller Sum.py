'''
Title     : Smaller Sum
Domain    : ???
Author    : Asmit Singh
Solved On   : 22 Apr 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def smallerSum(self, n: int, arr: List[int]) -> List[int]:
        dict = {}
        x = arr.copy()
        x.sort()
        s = 0
        ans = []
        for i in range(n):
            if x[i] not in dict:
                dict[x[i]] = s
            s += x[i]
        for i in arr:
            ans.append(dict[i])
        return ans
