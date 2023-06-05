'''
Title     : Find the Closest Element in BST
Author    : Asmit Singh
Solved On   : 05 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def minDiff(self, root, K):
        if root == None:
            return 1e9
        if root.data == K:
            return 0
        elif root.data < K:
            return min(abs(root.data-K), self.minDiff(root.right, K))
        else:
            return min(self.minDiff(root.left, K), abs(root.data-K))
