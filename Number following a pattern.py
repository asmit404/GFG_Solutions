"""
Title     : Number following a pattern
Author    : Asmit Singh
Solved On   : 10 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def printMinNumberForPattern(self, S):
        result = []
        stack = []
        num = 1
        for c in S:
            stack.append(num)
            num += 1
            if c == "I":
                result += [str(i) for i in stack[::-1]]
                stack = []
        stack.append(num)
        result += [str(i) for i in stack[::-1]]
        return int(''.join(result))

# Time Complexity: O(n)
# Space Complexity: O(n)