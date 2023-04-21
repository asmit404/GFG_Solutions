'''
Title     : Prefix Suffix String
Domain    : ???
Author    : Asmit Singh
Solved On   : 21 Apr 2023
Solved Using   : Python3
'''

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        res = set()
        ans = 0
        for s in s1:
            for i in range(len(s)):
                res.add(s[:i+1])
                res.add(s[i:])
        for s in s2:
            if s in res:
                ans += 1
        return ans
