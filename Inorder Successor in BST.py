"""
Title     : Inorder Successor in BST
Author    : Asmit Singh
Solved On   : 30 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def inorderSuccessor(self, root, X):
        if root is None or X is None: return None
        succ = None
        while root is not None:
            if root.data <= X.data:
                root = root.right
            else:
                succ = root
                root = root.left
        return succ