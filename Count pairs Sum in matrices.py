'''
Title     : Count pairs Sum in matrices
Author    : Asmit Singh
Solved On   : 11 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def countPairs(self, mat1, mat2, n, x):
        a = [j for i in mat1 for j in i]
        b = {j for i in mat2 for j in i}
        return sum(1 for i in a if x-i in b)

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)