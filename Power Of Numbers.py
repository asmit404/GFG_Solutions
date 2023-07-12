'''
Title     : Power Of Numbers
Author    : Asmit Singh
Solved On   : 12 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def power(self, N, R):
        mod = 1000000007
        res = 1
        while R > 0:
            if R % 2 == 1:
                res = (res * N) % mod
            N = (N * N) % mod
            R //= 2
        return res
