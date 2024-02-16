"""
Title     : Flatten BST to sorted list
Author    : Asmit Singh
Solved On   : 16 Feb 2024
Solved Using   : Python3
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def flattenBST(self, root):
        if not root: return None
        dummy = prev = Node(None)
        pool = []
        while root or pool:
            while root:
                pool.append(root)
                root = root.left
            root = pool.pop()
            root.left = None
            prev.right = root
            prev = root
            root = root.right
        return dummy.right

# Time Complexity: O(n)
# Space Complexity: O(n)