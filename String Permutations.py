"""
Title     : String Permutations
Author    : Asmit Singh
Solved On   : 06 Aug 2023
Solved Using   : Python3
"""

from itertools import permutations
class Solution:
    def permutation(self, s):
        return sorted([''.join(perm) for perm in permutations(s)])
    
# Time Complexity : O(n!)
# Space Complexity : O(n!)