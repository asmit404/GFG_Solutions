"""
Title     : Leaf under budget
Author    : Asmit Singh
Solved On   : 2 Sept 2023
Solved Using   : Python3
"""

from collections import deque
class Solution:
    def getCount(self, root, n):
        map = []
        pool = deque()
        pool.append(root)
        round = 1
        while pool:
            for _ in range(len(pool)):
                cur = pool.popleft()
                if not cur.left and not cur.right:
                    map.append((round, cur.data))
                if cur.left:
                    pool.append(cur.left)
                if cur.right:
                    pool.append(cur.right)
            round += 1
        ans, i = 0, 0
        while i < len(map) and ans <= n:
            ans += map[i][0]
            if ans <= n:
                i += 1
        return i

# Time Complexity: O(n)
# Space Complexity: O(m)