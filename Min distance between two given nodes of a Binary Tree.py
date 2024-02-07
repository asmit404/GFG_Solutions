"""
Title     : Min distance between two given nodes of a Binary Tree
Author    : Asmit Singh
Solved On   : 07 Feb 2024
Solved Using   : Python3
"""

class Solution:
    def findDist(self, root, a, b):
        def dist(node, target, level):
            if not node: return -1
            if node.data == target: return level
            left = dist(node.left, target, level + 1)
            if left != -1: return left
            return dist(node.right, target, level + 1)

        def lca(node, a, b):
            if not node: return None
            if node.data == a or node.data == b: return node
            left = lca(node.left, a, b)
            right = lca(node.right, a, b)
            if left and right: return node
            return left if left else right

        lca_node = lca(root, a, b)
        dist_a = dist(lca_node, a, 0)
        dist_b = dist(lca_node, b, 0)
        return dist_a + dist_b

# Time Complexity: O(n)
# Space Complexity: O(h)