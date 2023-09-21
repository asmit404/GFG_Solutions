"""
Title     : Stickler Thief
Author    : Asmit Singh
Solved On   : 21 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def FindMaxSum(self, a, n):
        prev_max = curr_max = 0
        for num in a:
            temp = curr_max
            curr_max = max(num + prev_max, curr_max)
            prev_max = temp
        return curr_max

# Very Practical Problem BTW.
# Time Complexity: O(n)
# Space Complexity: O(1)