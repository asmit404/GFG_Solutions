'''
Title     : Santa Banta
Author    : Asmit Singh
Solved On   : 02 Jun 2023
Solved Using   : Python3
'''

from collections import deque
a = 10**6
prime = [True for i in range(a + 1)]
primes = []

class Solution:
    def precompute(self):
        p = 2
        while (p * p <= a):
            if (prime[p] == True):
                for i in range(p * p, a + 1, p):
                    prime[i] = False
            p += 1
        for p in range(2, a + 1):
            if prime[p]:
                primes.append(p)

    def helpSanta(self, n, m, g):
        vis = [0]*(n+1)

        def bfs(i, vis):
            c = 1
            q = deque()
            q.append(i)
            vis[i] = 1
            while q:
                curr = q.popleft()
                for j in g[curr]:
                    if (not vis[j]):
                        vis[j] = 1
                        c += 1
                        q.append(j)
            return c
        max_ = 1
        for i in range(1, n+1):
            if (not vis[i]):
                max_ = max(max_, bfs(i, vis))
        return primes[max_-1] if max_ != 1 else -1

# 44 day streak broken lmao
# coz of this (https://www.youtube.com/watch?v=DrKA7sKOhws)