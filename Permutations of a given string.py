'''
Title     : Permutations of a given string
Author    : Asmit Singh
Solved On   : 09 Jun 2023
Solved Using   : Python3
'''

from itertools import permutations
class Solution:
    def find_permutation(self, S):
        ans = set()
        for i in permutations(S, len(S)):
            ans.add("".join(i))
        return sorted(list(ans))
