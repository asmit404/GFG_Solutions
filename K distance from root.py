'''
Title     : K distance from root
Author    : Asmit Singh
Solved On   : 3 May 2024
Solved Using   : Python3
'''

from collections import deque
class Solution:
    def KDistance(self, root, k):
        q = deque([root])
        pool = []
        while q and k >= 0:
            for _ in range(len(q)):
                node = q.popleft()
                if k == 0:
                    pool.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            k -= 1
        return pool

# Time Complexity: O(n)
# Space Complexity: O(n)