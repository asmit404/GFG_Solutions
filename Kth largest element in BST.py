"""
Title     : Kth largest element in BST
Author    : Asmit Singh
Solved On   : 9 Sept 2023
Solved Using   : Python3
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root, k):
        def reverse_inorder(root):
            if root == None:
                return
            reverse_inorder(root.right)
            if len(pool) < k:
                pool.append(root.data)
            reverse_inorder(root.left)
        pool = []
        reverse_inorder(root)
        return pool[-1]

# Time Complexity: O(n)
# Space Complexity: O(k)