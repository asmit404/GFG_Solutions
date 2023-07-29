"""
Title     : Median of BST
Author    : Asmit Singh
Solved On   : 29 Jul 2023
Solved Using   : Python3
"""

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.data)
        inorder_traversal(root.right, result)

def findMedian(root):
    result = []
    inorder_traversal(root, result)
    n = len(result)
    if n % 2 == 0:
        median1 = result[n // 2]
        median2 = result[n // 2 - 1]
        if (median1 + median2) % 2 == 0:
            return (median1 + median2) // 2
        return (median1 + median2) / 2
    return result[n // 2]
