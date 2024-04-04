'''
Title     : Sum of all substrings of a number
Author    : Asmit Singh
Solved On   : 4 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def sumSubstrings(self, s):
        MOD = 1000000007
        n = len(s)
        res = pos = 0
        for i in range(n):
            pos = (pos * 10 + int(s[i]) * (i + 1)) % MOD
            res = (res + pos) % MOD
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)