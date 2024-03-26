'''
Title     : Additive sequence
Author    : Asmit Singh
Solved On   : 26 Mar 2024
Solved Using   : Python3
'''

from itertools import combinations
class Solution:
    def isAdditiveSequence(self, n):
        def compute(a1, a2, s):
            if not s: return True
            a = a1 + a2
            return s.startswith(str(a)) and compute(a2, a, s[len(str(a)):])
        return int(any(compute(int(n[:i]), int(n[i:j]), n[j:]) for i, j in combinations(range(1, len(n)), 2)))

# Time Complexity: O(n ^ 3 * 2 ^ n)
# Space Complexity: O(n)