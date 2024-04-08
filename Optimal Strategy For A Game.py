'''
Title     : Optimal Strategy For A Game
Author    : Asmit Singh
Solved On   : 8 Apr 2024
Solved Using   : Python3
'''

from functools import lru_cache
from sys import setrecursionlimit

class Solution:
    def optimalStrategyOfGame(self, n, arr):
        setrecursionlimit(10**8)
        @lru_cache(None)
        def compute(s, e, flag):
            if s == e:
                if flag:
                    return arr[s], 0
                return 0, arr[s]
            if flag:
                a, b = compute(s+1, e, not flag)
                c, d = compute(s, e-1, not flag)
                c += arr[e]
                a += arr[s]
                return max((a, b), (c, d))
            a, b = compute(s+1, e, not flag)
            c, d = compute(s, e-1, not flag)
            b += arr[s]
            d += arr[e]
            if b > d:
                return (a, b)
            return (c, d)
        return compute(0, len(arr)-1, True)[0]

# I fckin hate recursion so much
# Time Complexity: O(n ^ 2)
# Space Complexity: O(n ^ 2)