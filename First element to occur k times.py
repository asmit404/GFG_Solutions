"""
Title     : First element to occur k times
Author    : Asmit Singh
Solved On   : 02 Mar 2024
Solved Using   : Python3
"""

class Solution:
    def firstElementKTime(self, n, k, a):
        d = {k: 0 for k in a}
        for i in a:
            d[i] += 1
            if d[i] == k:
                return i
            if max(d.values()) >= k:
                break
        return -1

# Time Complexity: O(n)
# Space Complexity: O(n)