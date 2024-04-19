'''
Title     : Find missing in second array
Author    : Asmit Singh
Solved On   : 19 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def findMissing(self, a, b, n, m):
        b = set(b)
        return [x for x in a if x not in b]

# Time Complexity: O(n + m)
# Space Complexity: O(m)