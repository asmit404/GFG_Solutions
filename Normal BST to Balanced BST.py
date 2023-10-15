"""
Title     : Normal BST to Balanced BST
Author    : Asmit Singh
Solved On   : 15 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def inOrderTraversal(self, node):
        return self.inOrderTraversal(node.left) + [node] + self.inOrderTraversal(node.right) if node else []

    def buildBalancedBST(self, nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = nodes[mid]
        root.left = self.buildBalancedBST(nodes[:mid])
        root.right = self.buildBalancedBST(nodes[mid + 1:])
        return root

    def buildBalancedTree(self, root):
        return self.buildBalancedBST(self.inOrderTraversal(root))

# Time Complexity: O(n)
# Space Complexity: O(n)