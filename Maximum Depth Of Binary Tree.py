'''
Title     : Maximum Depth Of Binary Tree
Author    : Asmit Singh
Solved On   : 28 Jun 2023
Solved Using   : Python3
'''

class Solution:
    def maxDepth(self, root):
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right)) if root else 0
