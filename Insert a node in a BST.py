"""
Title     : Insert a node in a BST
Author    : Asmit Singh
Solved On   : 10 Sept 2023
Solved Using   : Python3
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def insert(self, root, Key):
        if not root:
            return Node(Key)
        if root.data == Key:
            return root
        elif root.data < Key:
            root.right = self.insert(root.right, Key)
        else:
            root.left = self.insert(root.left, Key)
        return root

# Time Complexity: O(n)
# Space Complexity: O(h)