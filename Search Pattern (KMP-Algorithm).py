"""
Title     : Search Pattern (KMP-Algorithm)
Author    : Asmit Singh
Solved On   : 9 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def search(self, pat, txt):
        idx, n, m = [], len(txt), len(pat)
        for i in range(n - m + 1):
            if txt[i:i + m] == pat:
                idx.append(i + 1)
        return idx if idx else [-1]

# Didn't use KMP algorithm
# Time Complexity : O(n * m)
# Space Complexity : O(n)