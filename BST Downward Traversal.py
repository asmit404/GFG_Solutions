'''
Title     : BST Downward Traversal
Domain    : Data Structures
Author    : Asmit Singh
Solved On   : 06 Feb 2023
Solved Using   : Python3
'''

class Solution:
    def verticallyDownBST(self, root, target):
        def find(root, target):
            if root is None:
                return root
            if root.data == target:
                return root
            if root.data < target:
                return find(root.right, target)
            return find(root.left, target)
        def solve(root, dist):
            if root is None:
                return 0
            return solve(root.left, dist - 1) + solve(root.right, dist + 1) + (root.data if dist == 0 else 0)
        
        node = find(root, target)
        if node is None:
            return -1
        return solve(node, 0) - node.data
