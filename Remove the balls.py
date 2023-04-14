'''
Title     : Remove the balls
Domain    : Stack, Data Structures
Author    : Asmit Singh
Solved On   : 14 Apr 2023
Solved Using   : Python3
'''

from typing import List
class Solution:
    def finLength(self, N: int, color: List[int], radius: List[int]) -> int:
        stack = []
        stack.append((color[0], radius[0]))
        for i in range(1, len(color)):
            tmp = (color[i], radius[i])
            if len(stack) and stack[-1] == tmp:
                stack.pop()
            else:
                stack.append(tmp)
        return len(stack)
