'''
Title     : Express as sum of power of natural numbers
Author    : Asmit Singh
Solved On   : 26 May 2023
Solved Using   : Python3
'''

class Solution:
    def numOfWays(self, n, x):
        res = [0] * (n + 1)
        res[0] = 1
        MOD = 1000000007
        for i in range(1, n + 1):
            for j in range(n, i - 1, -1):
                y = i ** x
                if j >= y:
                    res[j] = (res[j] + res[j - y]) % MOD
        return res[n]
