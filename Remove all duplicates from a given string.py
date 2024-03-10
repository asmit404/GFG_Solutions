'''
Title     : Remove all duplicates from a given string
Author    : Asmit Singh
Solved On   : 10 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def removeDuplicates(self, str):
        seen = set()
        res = ""
        for i in str:
            if i not in seen:
                seen.add(i)
                res += i
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)