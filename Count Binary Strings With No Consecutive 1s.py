'''
Title     : Count Binary Strings With No Consecutive 1s
Author    : Asmit Singh
Solved On   : 9 May 2023
Solved Using   : Python3
'''

class Solution:
    mod = 10**9 + 7

    def result(self, n):
        if not n:
            return 0, 1
        a, b = self.result(n//2)
        c = (a*(b*2-a)) % self.mod
        d = (a*a + b*b) % self.mod
        if n % 2:
            return d, c+d
        return c, d

    def countStrings(self, N):
        ans, i = self.result(N+2)
        return ans % self.mod
