'''
Title     : Connect Nodes at Same Level
Domain    : Tree, Data Structures
Author    : Asmit Singh
Solved On   : 22 Feb 2023 // 31-Day streak broken lmao
Solved Using   : Python3
'''

from collections import deque
class Solution:
    def connect(self, root):
        dq = deque([root])
        levels = []
        while dq:
            level = []
            for _ in range(len(dq)):
                cur = dq.popleft()
                level.append(cur)
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            levels.append(level)
        for level in levels:
            for a,b in zip(level, level[1:]):
                a.nextRight = b
