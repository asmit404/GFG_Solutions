'''
Title     : Level order traversal
Author    : Asmit Singh
Solved On   : 18 Mar 2024
Solved Using   : Python3
'''

from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            n = len(queue)
            pool = []
            for _ in range(n):
                node = queue.popleft()
                pool.append(node.data)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.extend(pool)
        return res

# Time Complexity: O(n)
# Space Complexity: O(m)