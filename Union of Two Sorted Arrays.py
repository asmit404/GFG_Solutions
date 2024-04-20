'''
Title     : Union of Two Sorted Arrays
Author    : Asmit Singh
Solved On   : 20 Apr 2024
Solved Using   : Python3
'''

class Solution:
    def findUnion(self, arr1, arr2, n, m):
        return list(sorted(set(arr1).union(set(arr2))))

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)