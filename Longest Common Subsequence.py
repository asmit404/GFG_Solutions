"""
Title     : Longest Common Subsequence
Author    : Asmit Singh
Solved On   : 10 Aug 2023
Solved Using   : Python3
"""

class Solution:
    def lcs(self, x, y, s1, s2):
        prev = [0]*(y+1)
        curr = [0]*(y+1)
        for i in range(1, x+1):
            for j in range(1, y+1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev, curr = curr, prev
        return prev[y]

# Time Complexity : O(x*y)
# Space Complexity : O(y)
