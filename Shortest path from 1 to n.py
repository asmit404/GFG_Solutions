"""
Title     : Shortest path from 1 to n
Author    : Asmit Singh
Solved On   : 30 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def minimumStep(self, n):
        cnt = 0
        while n > 1:
            n = n // 3 if n % 3 == 0 else n - 1
            cnt += 1
        return cnt

# Time Complexity  : O(log n)
# Space Complexity : O(1)