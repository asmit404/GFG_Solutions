"""
Title     : Sum of leaf nodes in BST
Author    : Asmit Singh
Solved On   : 18 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def sumOfLeafNodes(self, root):
        if not root: return 0
        if not (root.left or root.right): return root.data
        a = self.sumOfLeafNodes(root.left)
        b = self.sumOfLeafNodes(root.right)
        return a + b

# Time Complexity: O(n)
# Space Complexity: O(h)