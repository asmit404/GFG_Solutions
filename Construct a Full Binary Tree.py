'''
Title     : Construct a Full Binary Tree
Author    : Asmit Singh
Solved On   : 23 May 2023
Solved Using   : Python3
'''

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        def build(pre, mirror):
            if not pre and not mirror:
                return None
            n = Node(pre[0])
            if len(pre) == 1:
                return n

            pre = pre[1:]
            mirror = mirror[1:]
            i, j = pre.index(mirror[0]), mirror.index(pre[0])
            n.left = build(pre[:i], mirror[j:])
            n.right = build(pre[i:], mirror[:j])
            return n
        return build(pre, preMirror)
