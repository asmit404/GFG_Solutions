"""
Title     : Chocolate Distribution Problem
Author    : Asmit Singh
Solved On   : 05 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def findMinDiff(self, A, N, M):
        A.sort()
        return min(A[i+M-1]-A[i] for i in range(N-M+1))

# Time Complexity: O(NlogN)
# Space Complexity: O(1)