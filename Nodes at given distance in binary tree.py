"""
Title     : Nodes at given distance in binary tree
Author    : Asmit Singh
Solved On   : 10 Oct 2023
Solved Using   : Python3
"""

from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def helper(self, node, target):
        if node.data == target and not self.target_node:
            self.target_node = node

        for child in [node.left, node.right]:
            if child:
                self.ancestor[child] = node
                self.helper(child, target)

    def KDistanceNodes(self, root, target, k):
        self.ancestor = {}
        self.target_node = None
        self.helper(root, target)

        q = deque([(self.target_node, 0)])
        res = []
        visited = {self.target_node}

        while q:
            node, distance = q.popleft()

            if distance == k:
                res.append(node.data)
                continue

            for child in [node.left, node.right, self.ancestor.get(node, None)]:
                if child and child not in visited:
                    q.append((child, distance+1))
                    visited.add(child)

        return sorted(res)

# Time Complexity: O(n)
# Space Complexity: O(n)