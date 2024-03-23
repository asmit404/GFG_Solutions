'''
Title     : Fibonacci series up to Nth term
Author    : Asmit Singh
Solved On   : 23 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def series(self, n):
        MOD = 1000000007
        res = [0, 1]
        t1, t2 = 0, 1
        for _ in range(n - 1):
            res.append((t1 + t2) % MOD)
            temp = (t1 + t2) % MOD
            t1 = t2
            t2 = temp
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)