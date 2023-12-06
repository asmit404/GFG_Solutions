"""
Title     : How Many X's?
Author    : Asmit Singh
Solved On   : 06 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def countX(self, L, R, X):
        return sum(str(i).count(str(X)) for i in range(L + 1, R))

# One Liner, but slower
# Time Complexity  : O(n)
# Space Complexity : O(1)