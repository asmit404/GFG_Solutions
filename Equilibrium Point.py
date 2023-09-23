"""
Title     : Equilibrium Point
Author    : Asmit Singh
Solved On   : 23 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def equilibriumPoint(self, A, N):
        rsum, lsum = sum(A), 0
        for i in range(N):
            rsum -= A[i]
            if lsum == rsum:
                return i + 1
            lsum += A[i]
        return -1

# Time Complexity: O(n)
# Space Complexity: O(1)