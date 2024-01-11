"""
Title     : Remove K Digits
Author    : Asmit Singh
Solved On   : 11 Jan 2024
Solved Using   : Python3
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        pool = []
        for digit in num:
            while k and pool and pool[-1] > digit:
                pool.pop()
                k -= 1
            pool.append(digit)
        pool = pool[:-k] if k else pool
        return ''.join(pool).lstrip('0') or '0'

# Time Complexity : O(n)
# Space Complexity : O(n)