"""
Title     : Floor in BST
Author    : Asmit Singh
Solved On   : 13 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def floor(self, root, x):
        if not root:
            return -1
        if root.data == x:
            return x
        if x > root.data:
            right = self.floor(root.right, x)
            return right if right != -1 else root.data
        return self.floor(root.left, x)

# Time Complexity: O(h)
# Space Complexity: O(h)