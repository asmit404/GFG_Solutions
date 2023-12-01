"""
Title     : Check whether BST contains Dead End
Author    : Asmit Singh
Solved On   : 01 Dec 2023
Solved Using   : Python3
"""

class Solution:
    def isDeadEnd(self, root):
        nodes = [root]
        vis, leaf = set(), set()

        while nodes:
            curr = nodes.pop()
            vis.add(curr.data)

            if not curr.left and not curr.right:
                leaf.add(curr.data)
                if (curr.data == 1 and 2 in vis) or (curr.data - 1 in vis and curr.data + 1 in vis):
                    return 1

            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)

        return 0

# Time Complexity  : O(n)
# Space Complexity : O(n)