"""
Title     : Find Common Nodes in two BSTs
Author    : Asmit Singh
Solved On   : 14 Oct 2023
Solved Using   : Python3
"""

class Solution:
    def findCommon(self, root1, root2):
        pool = []
        stack1, stack2 = [], []
        while True:
            if root1 is not None:
                stack1.append(root1)
                root1 = root1.left
            elif root2 is not None:
                stack2.append(root2)
                root2 = root2.left
            elif stack1 and stack2:
                node1, node2 = stack1[-1], stack2[-1]
                if node1.data == node2.data:
                    pool.append(node1.data)
                    root1, root2 = node1.right, node2.right
                    stack1.pop()
                    stack2.pop()
                elif node1.data < node2.data:
                    root1 = node1.right
                    stack1.pop()
                else:
                    root2 = node2.right
                    stack2.pop()
            else:
                break
        return pool

# Time Complexity: O(n1 + n2)
# Space Complexity: O(h1 + h2)