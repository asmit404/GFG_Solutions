'''
Title     : Palindrome with minimum sum
Author    : Asmit Singh
Solved On   : 11 May 2023
Solved Using   : Python3
'''

import math
class Solution:
    def minimumSum(self, s: str) -> int:
        i, j = 0, len(s)-1
        cur = None
        ans = 0
        while i <= j:
            if s[i] == '?' and s[j] == '?':
                i += 1
                j -= 1
                continue
            if s[i] == '?':
                if not cur:
                    cur = s[j]
                else:
                    ans += 2*abs(ord(cur)-ord(s[j]))
                    cur = s[j]
            elif s[j] == '?':
                if not cur:
                    cur = s[i]
                else:
                    ans += 2*abs(ord(cur)-ord(s[i]))
                    cur = s[i]
            else:
                if s[i] != s[j]:
                    return -1
                if not cur:
                    cur = s[i]
                else:
                    ans += 2*abs(ord(cur)-ord(s[i]))
                    cur = s[i]
            i += 1
            j -= 1
        return ans
