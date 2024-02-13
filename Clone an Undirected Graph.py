"""
Title     : Clone an Undirected Graph
Author    : Asmit Singh
Solved On   : 13 Feb 2024
Solved Using   : Python3
"""

from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10000)

class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution():
    def cloneGraph(self, node):
        newn = [None] * 10001
        newn[node.val] = Node(node.val, list())
        q = deque([node])
        while len(q) > 0:
            i = q.popleft()
            if len(newn[i.val].neighbors) == 0:
                for n in i.neighbors:
                    if newn[n.val] is None:
                        newn[n.val] = Node(n.val, list())
                    if len(newn[n.val].neighbors) == 0:
                        q.append(n)
                    newn[i.val].neighbors.append(newn[n.val])
        return newn[node.val]

# Time Complexity: O(N + E)
# Space Complexity: O(N + E)