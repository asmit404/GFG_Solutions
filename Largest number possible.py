"""
Title     : Largest number possible
Author    : Asmit Singh
Solved On   : 13 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def findLargest(self, N, S):
        if S == 0 and N > 1:
            return -1
        largest_num = ""
        while N > 0:
            if S < 9:
                largest_num += str(S)
                S = 0
            else:
                largest_num += str(9)
                S -= 9
            N -= 1
        return int(largest_num) if S == 0 else -1

# Time Complexity: O(n)
# Space Complexity: O(1)