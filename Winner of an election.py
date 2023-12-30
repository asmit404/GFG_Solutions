"""
Title     : Winner of an election
Author    : Asmit Singh
Solved On   : 30 Dec 2023
Solved Using   : Python3
"""

from collections import Counter

class Solution:
    def winner(self, arr, n):
        K = Counter(arr)
        max_val = max(K.values())
        winners = [k for k, v in K.items() if v == max_val]
        return min(winners), max_val

# Time Complexity  : O(n)
# Space Complexity : O(n)