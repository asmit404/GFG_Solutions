"""
Title     : Symmetric Tree
Author    : Asmit Singh
Solved On   : 22 Nov 2023
Solved Using   : Python3
"""

class Solution:
    def isSymmetricorNot(self, left, right):
        if left is None or right is None:
            return left is right
        if left.data != right.data:
            return False
        return (self.isSymmetricorNot(left.left, right.right) and
                self.isSymmetricorNot(left.right, right.left))

    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricorNot(root.left, root.right)

# Time Complexity : O(n)
# Space Complexity : O(h)