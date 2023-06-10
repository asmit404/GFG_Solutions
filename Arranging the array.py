'''
Title     : Arranging the array
Author    : Asmit Singh
Solved On   : 10 Jun 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def Rearrange(self, n: int, arr: List[int]) -> None:
        arr.sort(key=lambda x: x >= 0)
