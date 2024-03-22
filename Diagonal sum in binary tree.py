'''
Title     : Diagonal sum in binary tree
Author    : Asmit Singh
Solved On   : 22 Mar 2024
Solved Using   : Python3
'''

class Solution:
    def diagonalSum(self, root):
        dic = {}
        def traversal(root, d):
            if root is None: return
            dic[d] = dic.get(d, 0) + root.data
            traversal(root.right, d)
            traversal(root.left, d+1)
        traversal(root, 0)
        return list(dic.values())

# Time Complexity: O(n)
# Space Complexity: O(n)