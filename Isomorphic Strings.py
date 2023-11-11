"""
Title     : Isomorphic Strings
Author    : Asmit Singh
Solved On   : 11 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def areIsomorphic(self,str1,str2):
        if len(str1) == len(str2):
            d1, d2 = {}, {}
            for c1, c2 in zip(str1, str2):
                if (c1 in d1 and d1[c1] !=c2) or (c2 in d2 and d2[c2] != c1):
                    return False
                d1[c1] = c2
                d2[c2] = c1
            return True
        else:
            return False

# Time Complexity: O(n)
# Space Complexity: O(n)