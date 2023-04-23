'''
Title     : Minimum Number
Domain    : ???
Author    : Asmit Singh
Solved On   : 23 Apr 2023
Solved Using   : Python3
'''

import math
class Solution:
    def minimumNumber(self, n, arr):
        res = arr[0]
        for i in range(1, n):
            res = math.gcd(res, arr[i])
        return res
