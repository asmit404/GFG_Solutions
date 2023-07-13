'''
Title     : Unique Number of Occurrences
Author    : Asmit Singh
Solved On   : 13 Jul 2023
Solved Using   : Python3
'''

from typing import List
from collections import Counter
class Solution:
    def isFrequencyUnique(self, n: int, arr: List[int]) -> bool:
        c1 = Counter(arr)
        v1 = c1.values()
        c2 = Counter(v1)
        v2 = c2.values()
        return True if sum(v2) == len(v2) else False
