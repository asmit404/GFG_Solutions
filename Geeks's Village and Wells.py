'''
Title     : Easy Task
Author    : Asmit Singh
Solved On   : 27 Apr 2023
Solved Using   : Python3
'''

from typing import List
from collections import deque
class Solution:
    def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for i in range(n)]
        dist = [[-1] * m for i in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    q.append([i, j])
                    visited[i][j] = True
                if c[i][j] == 'W' or c[i][j] == '.' or c[i][j] == 'N':
                    dist[i][j] = 0
        dis = 2
        while q:
            size = len(q)
            for p in range(size):
                x = q.popleft()
                i = x[0]
                j = x[1]
                for k in range(4):
                    curri = i + dx[k]
                    currj = j + dy[k]
                    if curri >= 0 and currj >= 0 and curri < n and currj < m and visited[curri][currj] == False and c[curri][currj] != 'N':
                        visited[curri][currj] = True
                        q.append([curri, currj])
                        if c[curri][currj] == 'H':
                            dist[curri][currj] = dis
            dis += 2
        return dist
