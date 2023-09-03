"""
Title     : Check if Tree is Isomorphic
Author    : Asmit Singh
Solved On   : 3 Sept 2023
Solved Using   : Python3
"""

class Solution:
    def isIsomorphic(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        if root1.data != root2.data: return False

        leftIso = (self.isIsomorphic(root1.left, root2.left)
                   and self.isIsomorphic(root1.right, root2.right))
        flippedIso = (self.isIsomorphic(root1.left, root2.right)
                      and self.isIsomorphic(root1.right, root2.left))

        return leftIso or flippedIso

# Time Complexity: O(n ^ 2)
# Space Complexity: O(h)