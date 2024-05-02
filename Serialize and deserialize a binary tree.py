'''
Title     : Serialize and deserialize a binary tree
Author    : Asmit Singh
Solved On   : 2 May 2024
Solved Using   : Python3
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        def work(root):
            if not root: yield "#"
            else:
                yield root.data
                yield from work(root.left)
                yield from work(root.right)
        return list(work(root))

    def deSerialize(self, data):
        def work():
            val = next(data_iter)
            if val == "#": return None
            node = Node(val)
            node.left = work() # type: ignore
            node.right = work() # type: ignore
            return node
        data_iter = iter(data)
        return work()

# Time Complexity: O(n)
# Space Complexity: O(n)