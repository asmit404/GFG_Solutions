'''
Title     : Cutting Rectangles
Domain    : Mathematical, Combinatorial, Algorithms
Author    : Asmit Singh
Solved On   : 3 Mar 2023
Solved Using   : Python3
'''

import math
class Solution:
    def minimumSquares(self, L, B):
        x = math.gcd(L, B)
        return (L*B//(x*x), x)
