'''
Title     : Find Total Time Taken
Domain    : Arrays, Hash, Data Structures
Author    : Asmit Singh
Solved On   : 15 Apr 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def totalTime(self, n: int, arr: List[int], time: List[int]) -> int:
        ans = -1
        mp = {}
        for x in arr:
            if x in mp:
                mp[x] += 1
                ans += time[x-1]
            else:
                mp[x] = 1
                ans += 1
        return ans