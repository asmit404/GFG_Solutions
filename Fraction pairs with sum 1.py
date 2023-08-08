"""
Title     : Fraction pairs with sum 1
Author    : Asmit Singh
Solved On   : 08 Aug 2023
Solved Using   : Python3
"""

from math import gcd
class Solution:
    def countFractions(self, n, numerator, denominator):
        ans, hash = 0, {}
        for n, d in zip(numerator, denominator):
            g = gcd(n, d)
            n //= g
            d //= g
            ans += hash.get((d-n, d), 0)
            hash[(n, d)] = hash.get((n, d), 0)+1
        return ans

# Time Complexity : O(n log n)
# Space Complexity : O(n)
