'''
Title     : Taxi Booking
Domain    : Arrays, Greedy, Data Structures, Algorithms
Author    : Asmit Singh
Solved On   : 21 Mar 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def minimumTime(self, N: int, cur: int, pos: List[int], time: List[int]) -> int:
        l = []
        for i in range(N):
            l.append((abs(pos[i]-cur))*time[i])
        return min(l)
