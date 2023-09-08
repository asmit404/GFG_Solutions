"""
Title     : Binary Tree to BST
Author    : Asmit Singh
Solved On   : 8 Sept 2023
Solved Using   : Python3
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def binaryTreeToBST(self, root):
        def inorder_traversal(node, values):
            if not node:
                return
            inorder_traversal(node.left, values)
            values.append(node.data)
            inorder_traversal(node.right, values)

        def replace_values(node, values):
            if not node:
                return
            replace_values(node.left, values)
            node.data = values.pop(0)
            replace_values(node.right, values)

        values = []
        inorder_traversal(root, values)
        values.sort()
        replace_values(root, values)

# Time Complexity: O(N log N)
# Space Complexity: O(N)