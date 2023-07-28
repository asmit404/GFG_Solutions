"""
Title     : Lowest Common Ancestor in a BST
Author    : Asmit Singh
Solved On   : 28 Jul 2023
Solved Using   : Python3
"""

def LCA(root, n1, n2):
    if root.data == n1 or root.data == n2:
        return root
    elif (root.data < n1 and root.data > n2) or (root.data > n1 and root.data < n2):
        return root
    elif root.data > n1 and root.data > n2:
        return LCA(root.left, n1, n2)
    return LCA(root.right, n1, n2)
