"""
Title     : Make the array beautiful
Domain    : Arrays, Stack, Data Structures
Author    : Asmit Singh
Solved On   : 08 Apr 2023
Solved Using   : Python3
"""

from typing import List
class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        stack = []
        for e in arr:
            if stack and ((stack[-1] < 0 and e >= 0) or (stack[-1] >= 0 and e < 0)):
                stack.pop()
            else:
                stack.append(e)
        return stack
