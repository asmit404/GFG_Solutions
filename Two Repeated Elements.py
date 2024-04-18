'''
Title     : Two Repeated Elements
Author    : Asmit Singh
Solved On   : 18 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def twoRepeated(self, arr, n):
        vis, res = set(), []
        for num in arr:
            res.append(num) if num in vis else vis.add(num)
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)