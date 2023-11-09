"""
Title     : Predict the Column
Author    : Asmit Singh
Solved On   : 09 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def columnWithMaxZeros(self, arr, n):
        ans, idx = 0, -1
        for i in range(n):
            cnt_zero = sum(1 for j in range(n) if arr[j][i] == 0)
            if ans < cnt_zero:
                ans = cnt_zero
                idx = i
        return idx

# Time Complexity: O(n^2)
# Space Complexity: O(1)