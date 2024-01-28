"""
Title     : Geekina Hate 1s
Author    : Asmit Singh
Solved On   : 28 Jan 2024
Solved Using   : Python3
"""

from math import log2, factorial
class Solution:
    def __init__(self):
        self.comb_memo = {}

    def comb(self, n, r):
        if (n, r) in self.comb_memo:
            return self.comb_memo[(n, r)]
        result = factorial(n)//(factorial(r) * factorial(n-r)) if n >= r else 0
        self.comb_memo[(n, r)] = result
        return result

    def count_exact(self, a, k):
        if k == 0: return 1
        if a == 0: return 0
        m = int(log2(a))
        if m < k-1: return 0
        return self.comb(m, k) + self.count_exact(a ^ (1 << m), k-1)

    def count(self, a, k):
        return sum(self.count_exact(a, i) for i in range(k+1))

    def findNthNumber(self, n: int, k: int) -> int:
        lo, hi = 0, 10**18
        while lo < hi:
            mid = lo + (hi - lo)//2
            if self.count(mid, k) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo

# Time Complexity: O(log(n) * k * log(n))
# Space Complexity: O(n)