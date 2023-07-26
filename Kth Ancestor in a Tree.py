"""
Title     : Kth Ancestor in a Tree
Author    : Asmit Singh
Solved On   : 26 Jul 2023
Solved Using   : Python3
"""

def kthAncestor(root, k, node):
    q = [(root, [])]
    while q:
        n, p = q.pop(0)
        if n.data == node:
            return p[-k] if k <= len(p) else -1
        if n.left:
            q.append((n.left, p + [n.data]))
        if n.right:
            q.append((n.right, p + [n.data]))
    return -1
