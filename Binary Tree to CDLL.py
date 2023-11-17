"""
Title     : Binary Tree to CDLL
Author    : Asmit Singh
Solved On   : 17 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def find(self, a, v):
        if a is None: return
        self.find(a.left, v)
        v.append(a)
        self.find(a.right, v)

    def bTreeToClist(self, root):
        if root is None: return None
        v = []
        self.find(root, v)
        n = len(v)
        for i in range(n):
            v[i].left = v[(i - 1 + n) % n]
            v[i].right = v[(i + 1) % n]
        return v[0]

# Time Complexity : O(n)
# Space Complexity : O(n)