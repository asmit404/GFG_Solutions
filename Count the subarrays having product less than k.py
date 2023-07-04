'''
Title     : Count the subarrays having product less than k
Author    : Asmit Singh
Solved On   : 4 Jul 2023
Solved Using   : Python3
'''

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        res, prod, prev = 0, 1, 0
        for i in range(n):
            prod = prod*a[i]
            while prod >= k and prev <= i:
                prod = prod/(a[prev])
                prev = prev+1
            res = res + i - prev + 1
        return res
