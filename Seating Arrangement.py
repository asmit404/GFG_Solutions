'''
Title     : Seating Arrangement
Author    : Asmit Singh
Solved On   : 26 Apr 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def is_possible_to_get_seats(self, n: int, m: int, seats: List[int]) -> bool:
        for i in range(m):
            if seats[i] == 0:
                front_empty = False
                next_empty = False
                if i-1 < 0 or seats[i-1] == 0:
                    front_empty = True
                if i+1 >= m or seats[i+1] == 0:
                    next_empty = True
                if front_empty and next_empty:
                    n -= 1
                    seats[i] = 1
        if n <= 0:
            return True
        return False
