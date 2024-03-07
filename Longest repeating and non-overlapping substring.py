'''
Title     : Longest repeating and non-overlapping substring
Author    : Asmit Singh
Solved On   : 07 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def longestSubstring(self, s, n):
        res, maxi = "", -1
        for i in range(n):
            substr = ""
            for j in range(i, n):
                substr += s[j]
                if substr in s[j+1:]:
                    if maxi < len(substr):
                        maxi = len(substr)
                        res = substr
                else:
                    break
        return res if res != "" else "-1"

# Time Complexity: O(n ^ 3)
# Space Complexity: O(n)