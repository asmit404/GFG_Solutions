'''
Title     : Prefix match with other strings
Author    : Asmit Singh
Solved On   : 24 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def klengthpref(self, arr, n, k, s):
        return 0 if k > len(s) else [i[:k] for i in arr].count(s[:k])
