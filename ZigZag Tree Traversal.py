'''
Title     : ZigZag Tree Traversal
Author    : Asmit Singh
Solved On   : 21 Mar 2024
Solved Using   : Python3
'''

from collections import deque
class Solution:
    def zigZagTraversal(self, root):
        if not root: return []
        queue = deque([root])
        res = []
        check = False
        while queue:
            level = len(queue)
            val = []
            for _ in range(level):
                node = queue.popleft()
                val.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.extend(val[::-1] if check else val)
            check = not check
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)