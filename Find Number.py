'''
Title     : Find Number
Author    : Asmit Singh
Solved On   : 29 Apr 2023
Solved Using   : Python3
'''

class Solution:
    def findNumber(self, n: int) -> int:
        d = {1: 1, 2: 3, 3: 5, 4: 7, 0: 9}
        ans = 0
        multipler = 1
        while n > 0:
            r = n % 5
            n //= 5
            if r == 0:
                n -= 1
            ans += multipler * d[r]
            multipler *= 10
        return ans
