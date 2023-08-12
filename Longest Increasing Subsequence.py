"""
Title     : Longest Increasing Subsequence
Author    : Asmit Singh
Solved On   : 12 Aug 2023
Solved Using   : Python3
"""

import bisect
class Solution:
    def longestSubsequence(self,a,n):
        subsequence = [] 
        for num in a:
            index = bisect.bisect_left(subsequence, num)
            if index == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[index] = num
        return len(subsequence)

# Time Complexity : O(n log n)
# Space Complexity : O(n)