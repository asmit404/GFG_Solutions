"""
Title     : Leftmost and rightmost nodes of binary tree
Author    : Asmit Singh
Solved On   : 1 Sept 2023
Solved Using   : Python3
"""

from collections import deque
def printCorner(root):
    if not root:
        return

    pool = deque()
    pool.append(root)

    while pool:
        level_size = len(pool)
        for i in range(level_size):
            node = pool.popleft()

            if i == 0 or i == level_size - 1:
                print(node.data, end=" ")

            if node.left:
                pool.append(node.left)
            if node.right:
                pool.append(node.right)

# Time Complexity: O(n)
# Space Complexity: O(w)