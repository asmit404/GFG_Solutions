'''
Title     : nCr
Author    : Asmit Singh
Solved On   : 26 Jun 2023
Solved Using   : Python3
'''

pool = [1]
mod = 1000000007

class Solution:
    for i in range(1, 1001):
        pool.append(pool[~0] * i)

    def nCr(self, n, r):
        return (pool[n] // (pool[r] * pool[n - r])) % mod
