"""
Title     : Reverse First K elements of Queue
Author    : Asmit Singh
Solved On   : 12 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def modifyQueue(self, q, k):
        return q[:k][::-1] + q[k:]

# Time Complexity : O(n)
# Space Complexity : O(n)