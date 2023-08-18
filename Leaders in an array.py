"""
Title     : Leaders in an array
Author    : Asmit Singh
Solved On   : 18 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def leaders(self, A, N):
        pool = [A[-1]]
        for i in range(N-2, -1, -1):
            if pool[-1] <= A[i]:
                pool.append(A[i])
        return list(reversed(pool))

# Time Complexity: O(n)
# Space Complexity: O(n)