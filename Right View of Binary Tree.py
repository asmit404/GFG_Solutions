"""
Title     : Right View of Binary Tree
Author    : Asmit Singh
Solved On   : 24 Jul 2023
Solved Using   : Python3
"""

class Solution:
    def rightView(self, root):
        d = dict()
        self.func(root, d, 0)
        return d.values()

    def func(self, root, d, level):
        if root is None:
            return
        if level not in d:
            d[level] = root.data
        self.func(root.right, d, level + 1)
        self.func(root.left, d, level + 1)
